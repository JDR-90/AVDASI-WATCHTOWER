############################################################
#####              TELEMETRY_CSV_ROUTER.py             #####
############################################################

###
### Purpose: Logs telemetry data to a CSV file, including attitude, servo positions, and sensor readings, with timestamps.
###
### Script Dependencies: FC_CONNECT_ROUTER.py (for accessing telemetry API), ANGLE_CONVERSION.py (for converting raw sensor values to calibrated values based on kit-specific conversions)
###
### Library Dependencies: csv (for CSV file handling), os (for file path handling), time (for timing), threading (for concurrent logging), datetime (for timestamping), numpy (for data manipulation)
###
### See below for more detail on functionality 







import csv
import os
import time
import threading
from datetime import datetime
import numpy as np

import FC_CONNECT_ROUTER as FC_CONNECT
import ANGLE_CONVERSION as AC


# Global variables for logger state
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
_kit_number = None


# Converts the Hall Effect Senor raw value to the calibrated value based on the kit number
def _convert_sensor_value(raw_value, kit):

    if raw_value is None:
        return None
    
    # Kit-specific calibration/conversion factors
    # Adjust these values based on actual calibration data for each kit

    conversions = {
        7: lambda x: AC.sflap_sensor_linear(x) ,      # Kit 7 Conversion
        8: lambda x: AC.pflap_sensor_linear(x),       # Kit 8 Conversion
        9: lambda x: x,                               # Kit 9 Conversion
    }
    
    converter = conversions.get(kit, lambda x: x)  # Finds conversion function for the specified kit or defaults to no conversion
    return converter(raw_value)


# Generates a default CSV file path with a timestamp, placed in a telemetry folder in the Documents directory
def _default_csv_path(prefix="telemetry"):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    documents_dir = os.path.expanduser("~/Documents")
    telemetry_dir = os.path.join(documents_dir, "telemetry")
    
    # Create the telemetry folder if it doesn't exist
    os.makedirs(telemetry_dir, exist_ok=True)
    
    return os.path.join(telemetry_dir, f"{prefix}_{ts}.csv")


# Opens the CSV file and writes the header row. Returns the file object and CSV writer.
def _open_csv(path):
    f = open(path, "w", newline="")
    w = csv.writer(f)
    w.writerow([
        "rel_time",
        "current_time",
        "roll", "pitch", "yaw",
        "P_Flap (s1)", "P_Ail (s2)", "S_Flap (s3)", "S_Ail (s4)", "Rudder (s5)", "P_Elv (s6)", "S_Elv (s7)", "Sensor_Rel"
    ])
    f.flush()
    return f, w


# Writes a row of telemetry data to the CSV file based on the latest attitude, servo, and sensor data. 
# The timestamp is relative to the first logged entry
# Note that if the data is NoneType, it will be logged as an empty string ("") in the CSV to prevent errors

def _write_row(trigger_time):
    global _rows_since_flush, _t0

    if _t0 is None:
        _t0 = trigger_time
    
    rel_time = trigger_time - _t0

    # Get the latest data for attitude, servos and sensor
    att = FC_CONNECT.get_latest_attitude()
    srv = FC_CONNECT.get_latest_servos()
    flp_sensor = FC_CONNECT.get_latest_sensor()

    roll = pitch = yaw = ""

    # converts attitude from radians to degrees and stores in an array to be written to the CSV
    if att is not None:
        roll = "" if att[1] is None else np.degrees(att[1])
        pitch = "" if att[2] is None else np.degrees(att[2])
        yaw = "" if att[3] is None else np.degrees(att[3])

    # Adds servo values to an array to be written to the CSV
    servos = [""] * 8
    if srv is not None:
        for i in range(8):
            v = srv[1 + i]
            servos[i] = "" if v is None else v

    # Converts the raw sensor value to the calibrated value based on the kit number, and stores it in a variable to be written to the CSV
    sensor = ""
    if flp_sensor is not None:
        raw_sensor = flp_sensor[2]
        sensor = "" if raw_sensor is None else _convert_sensor_value(raw_sensor, _kit_number)



    current_time = datetime.now().strftime("%H:%M:%S")

    # Format of the row to be written: [relative time, current time, roll, pitch, yaw, 8 servo values, sensor value]
    row = [rel_time, current_time, roll, pitch, yaw] + servos + [sensor]




    # Attempts to write the row to the CSV file, and flushes the file every "_flush_every" rows. 
    # If an error occurs during writing or flushing, it is silently ignored to prevent crashes. 
    # The number of rows since the last flush is tracked with _rows_since_flush.

    try:
        _csv_writer.writerow(row)
        _rows_since_flush += 1
        if _rows_since_flush >= _flush_every:
            _csv_file.flush()
            _rows_since_flush = 0
    except Exception:
        pass




# Main loop of the csv logging thread. It continuously polls for new telemetry data at the specified frequency (poll_hz) 
# and writes it to the CSV file using _write_row() whenever new data is available.

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



# Function to start CSV logging. It initializes the CSV file, starts the logger thread, and sets up the necessary state.

def start_csv_logging(path=None, prefix="telemetry", flush_every=20, poll_hz=200, kit=None):
    global _thread, _csv_file, _csv_writer, _csv_path, _flush_every, _rows_since_flush
    global _last_att_t, _last_ser_t, _t0, _kit_number

    with _lock:
        if _thread is not None and _thread.is_alive():
            return _csv_path

        if path is None:
            path = _default_csv_path(prefix=prefix)
        
        # Use provided kit number, or get from FC_CONNECT_ROUTER if available
        if kit is None:
            try:
                _kit_number = FC_CONNECT.kit_number
            except AttributeError:
                _kit_number = None
        else:
            _kit_number = kit
        
        if _kit_number is not None:
            print(f"[CSV] Sensor conversion enabled for Kit {_kit_number}")

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



# Function to stop CSV logging. It signals the logger thread to stop, waits for it to finish, and closes the CSV file. It also resets the relevant state variables.
def stop_csv_logging():
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

