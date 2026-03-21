from pymavlink import mavutil
from ANGLE_CONVERSION import *

import threading, time

_override_lock = threading.Lock()
_override_active = False
_override_ch = [1500]*8  # last override packet



# Start a background thread to send override packets at 10 Hz

def start_override(m):
    global _override_active
    with _override_lock:
        if _override_active:
            return
        _override_active = True

    m.mav.rc_channels_override_send(m.target_system, m.target_component, 1500,1500,0,1500,0,500,0,0)

    def loop():
        # 10 Hz is plenty
        while True:
            with _override_lock:
                if not _override_active:
                    break
                ch = _override_ch.copy()
            m.mav.rc_channels_override_send(m.target_system, m.target_component, *ch)
            time.sleep(0.1)

    threading.Thread(target=loop, daemon=True).start()




# Stop sending override packets
def stop_override(m):
    global _override_active
    with _override_lock:
        _override_active = False
        _override_ch[:] = [0]*8
    # send once to clear immediately
    m.mav.rc_channels_override_send(m.target_system, m.target_component, 0,0,0,0,0,0,0,0)




# Functions to set angles for each control surface

def set_rudder(m, angle, yaw_ch=4):

    if not _override_active:
        start_override(m)

    # call this when UI sends a new command
    with _override_lock:
        
        _override_ch[yaw_ch-1] = int(def_to_rc(-1*angle, rc_normal, rudder_params))




def set_elevator(m, angle, pitch_ch=2):

    if not _override_active:
        start_override(m)

    # call this when UI sends a new command
    with _override_lock:
        
        _override_ch[pitch_ch-1] = int(def_to_rc(angle, rc_normal, elevator_params))




def set_p_aileron(m, angle, roll_ch=1):
    if not _override_active:
        start_override(m)

    # call this when UI sends a new command
    with _override_lock:
        
        _override_ch[roll_ch-1] = int(def_to_rc(angle, rc_normal, paileron_params))




def set_s_aileron(m, angle, roll_ch=1):
    if not _override_active:
        start_override(m)

    # call this when UI sends a new command
    with _override_lock:
        
        _override_ch[roll_ch-1] = int(def_to_rc(angle, rc_normal, saileron_params))




def set_p_flap(m, angle, flap_ch=5):
    if not _override_active:
        start_override(m)

    # call this when UI sends a new command
    with _override_lock:
        
        _override_ch[flap_ch-1] = int(def_to_rc(angle, rc_flaps, pflap_params))




def set_s_flap(m, angle, flap_ch=5):
    if not _override_active:
        start_override(m)

    # call this when UI sends a new command
    with _override_lock:
        
        _override_ch[flap_ch-1] = int(def_to_rc(angle, rc_flaps, sflap_params))
