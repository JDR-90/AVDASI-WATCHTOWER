############################################################
#####                ANGLE_COMMAND.py                  #####
############################################################

###
### Purpose: Controls servos by sending RC Override Packets with angles converted to RC values dependant on the kit connection
###
### Script Dependencies: ANGLE_CONVERSION.py (for converting angles to PWM values based on kit-specific conversions)
###
### Library Dependencies: threading (for concurrent execution), time (for timing)
###
### See below for more detail on functionality 







from ANGLE_CONVERSION import *
import threading, time

_override_lock = threading.Lock()   # To prevent other threads from modifying values in the override thread while sending packets
_override_active = False            # Whether the override thread should be running or not
_override_ch = [0,0,0,0,0,0,0,0]    # This is to pass-through the initial rc_channel values, as it varies depending on the kit (see below for default kit values for 0 deflection)




#          Roll, Pitch, Null, Yaw, Flap, Flap, Null, Null
# KIT 7 : [1426, 1506,   0,  1605, 1184, 1184,  0,    0]
# KIT 8 : [1330, 1506,   0,  1605, 1114, 1114,  0,    0]
# KIT 9 : [1426, 1506,   0,  1605, 1183, 1183,  0,    0]




################################################
##### RC Override Setup and Loop Functions #####
################################################

def start_override(m):

    global _override_active

    # Changes _override_active to True, which signals the thread to start sending packets. If it's already active, just return.
    with _override_lock:
        if _override_active:
            return
        _override_active = True

    
    # This is the loop that runs in the background as a thread to send the channel override packets (at 10Hz)
    def loop():

        while True:

            with _override_lock:
                # Check to see if thread should be active. If not, break out of loop and end thread.
                if not _override_active:
                    break

                ch = _override_ch.copy()

            m.mav.rc_channels_override_send(m.target_system, m.target_component, *ch)
            time.sleep(0.1)

    # Starts the override thread, daemon=True means it will automatically close when the main program exits
    threading.Thread(target=loop, daemon=True).start()




# Stop sending override packets
def stop_override(m):
    global _override_active

    with _override_lock:
        _override_active = False
        _override_ch[:] = [0]*8

    # send once to clear immediately
    m.mav.rc_channels_override_send(m.target_system, m.target_component, 0,0,0,0,0,0,0,0)





############################################################
##### Functions to set angles for each control surface #####
############################################################

# If commanded on UI and the override thread isn't already active, the thread will automatically activate. If already active it'll just update the values

def set_rudder(m, angle, yaw_ch=4):

    if not _override_active:
        start_override(m)

    with _override_lock:
        
        _override_ch[yaw_ch-1] = int(rudder_linear(angle))




def set_elevator(m, angle, pitch_ch=2):

    if not _override_active:
        start_override(m)

    with _override_lock:
        
        _override_ch[pitch_ch-1] = int(elevator_linear(angle))




def set_p_aileron(m, angle, roll_ch=1):
    if not _override_active:
        start_override(m)

    with _override_lock:
        
        _override_ch[roll_ch-1] = int(pail_deflection_get(angle))




def set_s_aileron(m, angle, roll_ch=1):
    if not _override_active:
        start_override(m)

    with _override_lock:
        
        _override_ch[roll_ch-1] = saileron_linear(angle)




def set_p_flap(m, angle, flap_ch=5):
    if not _override_active:
        start_override(m)

    with _override_lock:
        
        _override_ch[flap_ch-1] = pflap_linear(angle)




def set_s_flap(m, angle, flap_ch=5):
    if not _override_active:
        start_override(m)

    with _override_lock:
        
        _override_ch[flap_ch-1] = sflap_linear(angle)
