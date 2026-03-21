from pymavlink import mavutil


def command_mode(m, MODE):
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