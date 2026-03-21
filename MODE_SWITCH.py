############################################################
#####                   MODE_SWITCH.py                 #####
############################################################

###
### Purpose: Contains the function to send mode change commands to the flight controller via MAVLink, allowing switching between manual and stabilised (FBW-A) modes
###
### Script Dependencies: None
###
### Library Dependencies: pymavlink (for sending mode change commands)
###
### See below for more detail on functionality 







from pymavlink import mavutil


def command_mode(m, MODE):

    # 's' for stabilised (FBW-A), 'm' for manual
    if MODE == 's':
        MODE = 'FBWA'
    elif MODE == 'm':
        MODE = 'MANUAL'

    custom_mode_flag = mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED
    
    m.mav.command_long_send(
    m.target_component,
    m.target_system,
    mavutil.mavlink.MAV_CMD_DO_SET_MODE,
    0,
    custom_mode_flag,
    m.mode_mapping()[MODE],
    0,
    0,
    0,
    0,
    0
)