"""
TELEMETRY_CSV_ROUTER.py

CSV logging that works with the *router pattern*.

- Expects FC_CONNECT_ROUTER to already be running and populating latest snapshots + history buffers.
- It runs its own lightweight logger thread that polls the router's latest 
  attitude/servo snapshots and writes merged rows to CSV.


Expects API (from FC_CONNECT_ROUTER):
- get_latest_attitude() -> (t, roll, pitch, yaw) or None
- get_latest_servos()   -> (t, s1..s8) or None

Usage (from your UI, after router starts):
    import FC_CONNECT_ROUTER as FC_CONNECT
    import TELEMETRY_CSV_ROUTER as TLOG

    FC_CONNECT.run_status_refresh(self.mavlink)
    csv_path = TLOG.start_csv_logging(prefix="telemetry", flush_every=20)

    # on close:
    TLOG.stop_csv_logging()

Notes:
- This logger writes a row when it detects a NEW attitude sample or NEW servo sample.
- Each row is a merged "latest snapshot" at that moment.
"""

import csv
import os
import time
import threading
from datetime import datetime
import numpy as np

import FC_CONNECT_ROUTER as FC_CONNECT
import Reading_flap_angle as FLP_SENSOR


_lock = threading.Lock()
_stop_event = threading.Event()
_thread = None

_csv_file = None
_csv_writer = None
_csv_path = None

_flush_every = 20
_rows_since_flush = 0

_last_att_t = None
_last_ser_t = None
_last_sensor_t = None

_t0 = None

def _default_csv_path(prefix="telemetry"):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, f"{prefix}_{ts}.csv")


def _open_csv(path):
    f = open(path, "w", newline="")
    w = csv.writer(f)
    w.writerow([
        "rel_time",
        "current_time",
        "roll", "pitch", "yaw",
        "servo1", "servo2", "servo3", "servo4", "servo5", "servo6", "servo7", "servo8", "Sensor_Raw"
    ])
    f.flush()
    return f, w


def _write_row(trigger_time):
    global _rows_since_flush, _t0

    if _t0 is None:
        _t0 = trigger_time
    
    rel_time = trigger_time - _t0

    att = FC_CONNECT.get_latest_attitude()
    srv = FC_CONNECT.get_latest_servos()
    flp_sensor = FC_CONNECT.get_latest_sensor()

    roll = pitch = yaw = ""
    if att is not None:
        roll = "" if att[1] is None else np.degrees(att[1])
        pitch = "" if att[2] is None else np.degrees(att[2])
        yaw = "" if att[3] is None else np.degrees(att[3])

    servos = [""] * 8
    if srv is not None:
        for i in range(8):
            v = srv[1 + i]
            servos[i] = "" if v is None else v

    sensor = ""
    if flp_sensor is not None:
        sensor = "" if flp_sensor[2] is None else flp_sensor[2]

    current_time = datetime.now().strftime("%H:%M:%S")

    row = [rel_time, current_time, roll, pitch, yaw] + servos + [sensor]

    try:
        _csv_writer.writerow(row)
        _rows_since_flush += 1
        if _rows_since_flush >= _flush_every:
            _csv_file.flush()
            _rows_since_flush = 0
    except Exception:
        pass


def _logger_loop(poll_hz=500):
    global _last_att_t, _last_ser_t, _last_sensor_t

    poll_hz = max(10, int(poll_hz))
    period = 1.0 / poll_hz

    while not _stop_event.is_set():
        att = FC_CONNECT.get_latest_attitude()
        srv = FC_CONNECT.get_latest_servos()
        flp_sensor = FC_CONNECT.get_latest_sensor()

        wrote = False

        if att is not None:
            t_att = att[0]
            if _last_att_t is None or t_att > _last_att_t:
                _last_att_t = t_att
                _write_row(t_att)
                wrote = True

        if srv is not None:
            t_srv = srv[0]
            if _last_ser_t is None or t_srv > _last_ser_t:
                _last_ser_t = t_srv
                if not wrote or t_srv != _last_att_t:
                    _write_row(t_srv)
                    wrote=True

        if flp_sensor is not None:
            t_flp = flp_sensor[0]
            if _last_sensor_t is None or t_flp > _last_sensor_t:
                _last_sensor_t = t_flp
                if not wrote or t_flp != _last_att_t:
                    _write_row(t_flp)

        time.sleep(period)


def start_csv_logging(path=None, prefix="telemetry", flush_every=20, poll_hz=200):
    """
    Start CSV logging in a background thread.

    Returns the csv path in use.
    """
    global _thread, _csv_file, _csv_writer, _csv_path, _flush_every, _rows_since_flush
    global _last_att_t, _last_ser_t, _t0

    with _lock:
        if _thread is not None and _thread.is_alive():
            return _csv_path

        if path is None:
            path = _default_csv_path(prefix=prefix)

        _flush_every = max(1, int(flush_every))
        _rows_since_flush = 0
        _last_att_t = None
        _last_ser_t = None

        _csv_file, _csv_writer = _open_csv(path)
        _csv_path = path

        _stop_event.clear()
        _thread = threading.Thread(target=_logger_loop, args=(poll_hz,), daemon=True)
        _thread.start()

    print(f"[CSV] Telemetry logger started: {_csv_path}")
    return _csv_path


def stop_csv_logging():
    """
    Stop the logger thread and close the CSV file.
    Returns the closed path (or None if not running).
    """
    global _csv_file, _csv_writer, _csv_path, _thread

    with _lock:
        if _thread is None:
            return None

        _stop_event.set()
        try:
            _thread.join(timeout=1.5)
        except Exception:
            pass
        _thread = None

        closed = _csv_path

        try:
            if _csv_file is not None:
                _csv_file.flush()
        except Exception:
            pass
        try:
            if _csv_file is not None:
                _csv_file.close()
        except Exception:
            pass

        _csv_file = None
        _csv_writer = None
        _csv_path = None

    print(f"[TELEM] Telemetry logger stopped")
    return closed


def is_logging():
    with _lock:
        return _thread is not None and _thread.is_alive()



def on_plot_close(event=None):
    # stop the csv logger thread and close the file
    closed = stop_csv_logging()
    if closed:
        print("[CSV] CSV saved:", closed)

