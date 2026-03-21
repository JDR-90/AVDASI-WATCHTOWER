from math import degrees
from pymavlink import mavutil
from ANGLE_CONVERSION import *

port_config = {"TO": 20,
               "CR": 0,
               "LD": 30}


star_config = {"TO": 20,
               "CR": 0,
               "LD": 30}




def send_servo_command(connection, servo_number, pwm_value):
    """
    Sends the MAV_CMD_DO_SET_SERVO command to the Orange Cube.
    """
    connection.mav.command_long_send(
        connection.target_system,
        connection.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
        0,              # Confirmation
        servo_number,   # The Servo Number (Main_Out 1, 2, etc.)
        pwm_value,      # The Calculated PWM
        0, 0, 0, 0, 0   # Unused parameters
    )




def set_flaps(connection, angle):
    """
    Allows setting Port and Starboard flaps to different angles.
    Useful for reversing one side or trimming mechanical differences.
    """
    # 1. Calculate PWM for Port
    port_pwm = pflap_atp(angle)
    
    # 2. Calculate PWM for Starboard
    starboard_pwm = sflap_atp(angle)

    # 3. Send commands
    send_servo_command(connection, 1, port_pwm)      # Main_Out 1
    send_servo_command(connection, 3, starboard_pwm) # Main_Out 3





def flaps_mode(connection, mode):
    """
    Sets flaps to predefined positions based on mode.
    Modes: "TO" (Takeoff), "CR" (Cruise), "LD" (Landing)
    """
    if mode == "TO":
        port_angle = port_config["TO"]
        star_angle = star_config["TO"]
    elif mode == "CR":
        port_angle = port_config["CR"]
        star_angle = star_config["CR"]
    elif mode == "LD":
        port_angle = port_config["LD"]
        star_angle = star_config["LD"]


    # Calculate PWM values
    port_pwm = pflap_atp(port_angle)
    star_pwm = sflap_atp(star_angle)

    # Send commands
    send_servo_command(connection, 1, port_pwm)      # Main_Out 1
    send_servo_command(connection, 3, star_pwm)      # Main_Out 3