\
"""
FC_CONNECT.py

One background thread reads MAVLink messages (recv_match) and stores:
- Latest status text / heartbeat
- Rolling history deques for ATTITUDE and SERVO_OUTPUT_RAW

Other parts of the program (UI, telemetry plotter, logger) MUST NOT call recv_match().
They should read data via the getter functions in this module.

This avoids "message stealing" between threads.
"""

from pymavlink import mavutil
import threading
import time
from collections import deque

# -----------------------------
# Connection
# -----------------------------

def connection_start(kit=None):
    """
    Creates the MAVLink connection and waits for a heartbeat.
    Returns mavutil connection object (m), or None on failure.
    """
    if kit is None:
        kit = "8"
    kit = str(kit)

    if kit == "8":
        m = mavutil.mavlink_connection("udp:0.0.0.0:14558")
    elif kit == "7":
        m = mavutil.mavlink_connection("udp:0.0.0.0:14557")
    else:
        raise ValueError(f"Unknown kit '{kit}' (expected '7' or '8').")

    print("[CONNECT] Waiting for heartbeat...")
    try:
        hb = m.wait_heartbeat(timeout=10)
    except Exception as e:
        print(f"[CONNECT] Heartbeat not received: {e}")
        return None

    print("[CONNECT] Heartbeat received.")

    # IMPORTANT: set target sys/comp from the heartbeat source
    m.target_system = hb.get_srcSystem()
    m.target_component = hb.get_srcComponent()
    print(f"[CONNECT] Target set to sys={m.target_system} comp={m.target_component}")


    # After heartbeat received, request faster streams
    # MAVLink message IDs:
    # ATTITUDE = 30
    # SERVO_OUTPUT_RAW = 36

    def _set_msg_hz(m, msg_id, hz):
        interval_us = int(1_000_000 / hz)
        m.mav.command_long_send(
            m.target_system,
            m.target_component,
            mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,
            0,
            msg_id,          # param1: message id
            interval_us,     # param2: interval (microseconds)
            0, 0, 0, 0, 0
        )




    try:
        time.sleep(0.2)  # brief pause before changing rates

        for _ in range(3):
            _set_msg_hz(m, 30, 50)          # ATTITUDE at 30 Hz (>=20 Hz target) (first '30' is message ID for ATTITUDE)
            _set_msg_hz(m, 36, 50)          # SERVO_OUTPUT_RAW at 30 Hz          ('36' is message ID for SERVO_OUTPUT_RAW)
            time.sleep(0.05)

        print("[CONNECT] Sucessful message frequency change")




    except Exception as e:
        print("[CONNECT] Failed to set message intervals:", e)

        # --- fallback method ---
        m.mav.request_data_stream_send(
            m.target_system,
            m.target_component,
            mavutil.mavlink.MAV_DATA_STREAM_EXTRA1,
            30,
            1
        )

        print("[CONNECT] Requested data streams at 30Hz (fallback)")



    return m


# -----------------------------
# Router state (shared buffers)
# -----------------------------

_lock = threading.Lock()
_stop_event = threading.Event()
_router_thread = None

# Rolling histories (time, ...)
_attitude_hist = deque(maxlen=600)  # (time_now, roll, pitch, yaw)
_servo_hist = deque(maxlen=600)     # (time_now, s1..s8)

# Latest snapshot values of each data type
_latest = {
    "heartbeat": None,   # (time_now, msg_dict-ish)
    "statustext": None,  # (time_now, text, severity)
    "attitude": None,    # (time_now, roll, pitch, yaw)
    "servos": None,      # (time_now, s1..s8)
}

# -----------------------------
# Router loop
# -----------------------------

def _router_loop(m):
    """
    Reads ALL MAVLink messages and routes them into buffers.
    This must be the only place in your program that calls recv_match().
    """

    # To check message frequency
    att_n = 0
    srv_n = 0
    rate_t0 = time.time()


    # Use a timeout so we can notice stop_event and exit cleanly.
    while not _stop_event.is_set():
        try:
            msg = m.recv_match(type=["ATTITUDE", "SERVO_OUTPUT_RAW", "HEARTBEAT", "STATUSTEXT"], blocking=True, timeout=0.5)
        except Exception:
            msg = None


        now = time.time()
        if now - rate_t0 >= 10:
            print(f"[TELEM_STATS] ATTITUDE={att_n/10} Hz, SERVO_OUTPUT_RAW={srv_n/10} Hz")
            att_n = 0
            srv_n = 0
            rate_t0 = now

        if msg is None:
            continue

        time_now = time.time()
        mtype = msg.get_type()

        # Note: we keep critical sections very short.
        if mtype == "ATTITUDE":
            att_n += 1

            roll = getattr(msg, "roll", None)
            pitch = getattr(msg, "pitch", None)
            yaw = getattr(msg, "yaw", None)
            sample = (time_now, roll, pitch, yaw)
            with _lock:
                _latest["attitude"] = sample
                _attitude_hist.append(sample)

        elif mtype == "SERVO_OUTPUT_RAW":
            srv_n += 1
            # SERVO_OUTPUT_RAW has fields servo1_raw...servo8_raw
            s = []
            for i in range(1, 9):
                s.append(getattr(msg, f"servo{i}_raw", None))
            sample = (time_now,) + tuple(s)
            with _lock:
                _latest["servos"] = sample
                _servo_hist.append(sample)

        elif mtype == "STATUSTEXT":
            text = getattr(msg, "text", "")
            severity = getattr(msg, "severity", None)
            with _lock:
                _latest["statustext"] = (time_now, text, severity)

        elif mtype == "HEARTBEAT":
            # Store minimal heartbeat info
            hb = {
                "base_mode": getattr(msg, "base_mode", None),
                "custom_mode": getattr(msg, "custom_mode", None),
                "system_status": getattr(msg, "system_status", None),
                "type": getattr(msg, "type", None),
                "autopilot": getattr(msg, "autopilot", None),
            }
            with _lock:
                _latest["heartbeat"] = (time_now, hb)







# -----------------------------
# Public API
# -----------------------------

def run_status_refresh(m, maxlen=600):
    """
    Starts the router thread if not already running.
    """
    global _router_thread, _attitude_hist, _servo_hist

    with _lock:
        _attitude_hist = deque(_attitude_hist, maxlen=maxlen)
        _servo_hist = deque(_servo_hist, maxlen=maxlen)

    if _router_thread is not None and _router_thread.is_alive():
        return

    _stop_event.clear()
    _router_thread = threading.Thread(target=_router_loop, args=(m,), daemon=True)
    _router_thread.start()
    print("Started MAVLink router thread.")


def stop_router():
    """
    Requests the router thread to stop.
    """
    _stop_event.set()


def get_latest_attitude():
    with _lock:
        return _latest["attitude"]


def get_latest_servos():
    with _lock:
        return _latest["servos"]


def get_latest_statustext():
    with _lock:
        return _latest["statustext"]


def get_latest_heartbeat():
    with _lock:
        return _latest["heartbeat"]


def copy_attitude_history():
    """
    Returns a copy (list) of the rolling attitude history.
    Safe to use without holding locks elsewhere.
    """
    with _lock:
        return list(_attitude_hist)


def copy_servo_history():
    with _lock:
        return list(_servo_hist)


def find_servo_pos(cs_name):
    """
    Returns the index of the servo corresponding to the control surface name.
    """


    dictionary = {
        "time":             0,
        "p_flap":           1,
        "p_aileron":        2,
        "s_flap":           3,
        "s_aileron":        4,
        "rudder":           5,
        "p_elevator":       6,
        "s_elevator":       7 }
    
    return dictionary[cs_name]