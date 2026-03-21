from pymavlink import mavutil
from ANGLE_CONVERSION import *
from FC_CONNECT_ROUTER import kit_number

import threading, time

_override_lock = threading.Lock()
_override_active = False
_override_ch = [1500,1506,0,1605,500,500,0,0]  # last override packet, rc8 (mode toggle) always 0 to keep manual mode



# Start a background thread to send override packets at 10 Hz

def start_override(m):
    global _override_active
    with _override_lock:
        if _override_active:
            return
        _override_active = True

    #if kit_number == 7:
    #    flap = 1183
    #    ail = 1454
    #elif kit_number == 8:
    #    flap = 500
    #    ail = 1500
    #elif kit_number == 9:
    #    flap = 500
    #    ail = 1500
    
    m.mav.rc_channels_override_send(m.target_system, m.target_component, 1500,1506,0,1605,500,500,0,0) # CHANGE '500' BETWEEN S WING AND P WING BEFORE WIND TUNNEL TEST!!!!!!!!

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
        
        _override_ch[yaw_ch-1] = int(rudder_linear(angle))




def set_elevator(m, angle, pitch_ch=2):

    if not _override_active:
        start_override(m)

    # call this when UI sends a new command
    with _override_lock:
        
        _override_ch[pitch_ch-1] = int(elevator_linear(angle))




def set_p_aileron(m, angle, roll_ch=1):
    if not _override_active:
        start_override(m)

    # call this when UI sends a new command
    with _override_lock:
        
        _override_ch[roll_ch-1] = pail_deflection_get(angle)




def set_s_aileron(m, angle, roll_ch=1):
    if not _override_active:
        start_override(m)

    # call this when UI sends a new command
    with _override_lock:
        
        _override_ch[roll_ch-1] = int(sail_deflection_get(angle))




def set_p_flap(m, angle, flap_ch=5):
    if not _override_active:
        start_override(m)

    # call this when UI sends a new command
    with _override_lock:
        
        _override_ch[flap_ch-1] = pflap_linear(angle)




def set_s_flap(m, angle, flap_ch=5):
    if not _override_active:
        start_override(m)

    # call this when UI sends a new command
    with _override_lock:
        
        _override_ch[flap_ch-1] = int(sflap_deflection_get(angle))
