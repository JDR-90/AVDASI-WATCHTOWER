############################################################
#####                FC_CONNECT_ROUTER.py              #####
############################################################

###
### Purpose: Provides the connection to the relative cube, extracts the relevant telemetry data and stores in a buffer, 
###          and provides an API for other modules to access the latest values
###
### Script Dependencies: ANGLE_COMMAND.py (for the servo override values)
###
### Library Dependencies: pymavlink (for MAVLink communication), threading (for concurrent tasks), time (for timing), datetime (for timestamping), collections (for data buffering)
###
### See below for more detail on functionality 






from pymavlink import mavutil
import threading
import time
import datetime
from collections import deque
from ANGLE_COMMAND import _override_ch


# Global kit connection object
kit_number = None



# -----------------------------
# Connection
# -----------------------------

def connection_start(kit=None):
    global kit_number



    if kit is None:
        kit = "7"
    kit = str(kit)


    # Connects to the appropriate UDP port based on the kit number and sets initial servo override values.
    if kit == "8":
        kit_number = 8
        m = mavutil.mavlink_connection("udp:0.0.0.0:14558", timeout=5)
        _override_ch[:] = [1330,1506,0,1605,1114,1114,0,0]
    elif kit == "7":
        kit_number = 7
        m = mavutil.mavlink_connection("udp:0.0.0.0:14557", timeout=5)
        _override_ch[:] = [1426,1506,0,1605,1184,1184,0,0]
    elif kit == "9":
        kit_number = 9
        m = mavutil.mavlink_connection("udp:0.0.0.0:14559", timeout=5)
        _override_ch[:] = [1426,1506,0,1605,1183,1183,0,0]

    else:
        raise ValueError(f"Unknown kit '{kit}' (expected '7', '8', '9').")

    print("[CONNECT] Waiting for heartbeat...")
    try:
        hb = m.wait_heartbeat(timeout=5)
    except Exception as e:
        print(f"[CONNECT] Heartbeat not received: {e}")
        return None

    # IMPORTANT: set target sys/comp from the heartbeat source
    m.target_system = hb.get_srcSystem()
    m.target_component = hb.get_srcComponent()
    print(f"[CONNECT] Heartbeat received.")
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
            _set_msg_hz(m, 36, 50)    
            _set_msg_hz(m,249, 50)  
            _set_msg_hz(m,251, 50)          # NAMED_VALUE_FLOAT at 50 Hz ('251' is message ID for NAMED_VALUE_FLOAT)
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

# Rolling histories (time, ...) buffers
_attitude_hist = deque(maxlen=600)  # (time_now, roll, pitch, yaw)
_servo_hist = deque(maxlen=600)     # (time_now, s1..s8)

# Latest snapshot values of each data type
_latest = {
    "heartbeat": None,   # (time_now, msg_dict-ish)
    "statustext": None,  # (time_now, text, severity)
    "attitude": None,    # (time_now, roll, pitch, yaw)
    "servos": None,      # (time_now, s1..s8)
    "SENSOR": None,  # (time_now, name, value)
}

# -----------------------------
# Router loop - Extracts latest values and adds to the buffers and "_latest" snapshots
# -----------------------------

def _router_loop(m):

    # To check message frequency
    att_n = 0
    srv_n = 0
    rate_t0 = time.time()


    # Use a timeout so we can notice stop_event and exit cleanly.
    while not _stop_event.is_set():
        try:
            msg = m.recv_match(type=["ATTITUDE", "SERVO_OUTPUT_RAW", "HEARTBEAT", "NAMED_VALUE_FLOAT"], blocking=True, timeout=0.01)
        except Exception:
            msg = None


        now = time.time()
        if now - rate_t0 >= 10:

            print(f"[TIME] Current time: {datetime.datetime.now().strftime('%H:%M:%S')}")
            print(f"[TELEM_STATS] ATTITUDE={round(att_n/30, 2)} Hz, SERVO_OUTPUT_RAW={round(srv_n/30, 2)} Hz \n")
            att_n = 0
            srv_n = 0
            rate_t0 = now

        if msg is None:
            continue

        time_now = time.time()
        mtype = msg.get_type()


        # Attitude data handling: store roll, pitch, yaw in both the latest snapshot and the rolling history buffer.
        if mtype == "ATTITUDE":
            att_n += 1
            roll = getattr(msg, "roll", None)
            pitch = getattr(msg, "pitch", None)
            yaw = getattr(msg, "yaw", None)
            sample = (time_now, roll, pitch, yaw)
            with _lock:
                _latest["attitude"] = sample
                _attitude_hist.append(sample)


        # Servo output handling: store servo outputs in both the latest snapshot and the rolling history buffer.
        elif mtype == "SERVO_OUTPUT_RAW":
            srv_n += 1
            s = []
            for i in range(1, 9):
                s.append(getattr(msg, f"servo{i}_raw", None))
            sample = (time_now,) + tuple(s)
            with _lock:
                _latest["servos"] = sample
                _servo_hist.append(sample)


        # Status text handling: store the latest status text and severity in the snapshot. 
        # Good for debugging and seeing what parameters are being recived from the cube
        elif mtype == "STATUSTEXT":
            text = getattr(msg, "text", "")
            severity = getattr(msg, "severity", None)
            with _lock:
                _latest["statustext"] = (time_now, text, severity)


        # Heartbeat handling: store the latest heartbeat info in the snapshot.
        elif mtype == "HEARTBEAT":
            hb = {
                "base_mode": getattr(msg, "base_mode", None),
                "custom_mode": getattr(msg, "custom_mode", None),
                "system_status": getattr(msg, "system_status", None),
                "type": getattr(msg, "type", None),
                "autopilot": getattr(msg, "autopilot", None),
            }
            with _lock:
                _latest["heartbeat"] = (time_now, hb)

        # Parameter NAMED_VALUE_FLOAT stores the sensor data. The value stored in the snapshot
        elif mtype == "NAMED_VALUE_FLOAT":
            
            sensor_name = getattr(msg, "name", "").strip('\x00')
            sensor_value = getattr(msg, "value", None)
            
            with _lock:
                _latest["SENSOR"] = (time_now, sensor_name, sensor_value)




# -----------------------------
# Public API - Functions for accessing the latest values and starting/stopping the router thread.
# -----------------------------

def run_status_refresh(m, maxlen=600):
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
    _stop_event.set()



# Accessing the latest values
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


def get_latest_sensor():    
    with _lock:
        return _latest["SENSOR"]
    

# Returns a copy of the rolling history buffers for attitude and servo data. Useful for analysis/debugging without affecting the live data collection.
def copy_attitude_history():

    with _lock:
        return list(_attitude_hist)


def copy_servo_history():
    with _lock:
        return list(_servo_hist)



# dictionary to find the index of the servo corresponding to the control surface name. Time added also for easier debugging 
def find_servo_pos(cs_name):
    
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