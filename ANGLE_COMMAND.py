from pymavlink import mavutil
from ANGLE_CONVERSION import *


pinlayout = {
          "p_flap": 1,
          "p_aileron": 2,
          "s_flap": 3,
          "s_aileron": 4,
          "rudder": 5,
          "p_elevator": 6,
          "s_elevator": 7 
          }




# flap conrtol has its own script


## MAX:2500 MIN:500  180 degress rotation of servo
def set_rudder(m, angle):
    m.mav.command_long_send(
    m.target_system, m.target_component,
    mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
    0,
    pinlayout['rudder'],
    rudder_atp(angle),
    0,0,0,0,0)
    
def set_elevator(m, angle):
    m.mav.command_long_send(
    m.target_system, m.target_component,
    mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
    0,
    pinlayout['p_elevator'],
    elevator_atp(angle),
    0,0,0,0,0)


    m.mav.command_long_send(
    m.target_system, m.target_component,
    mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
    0,
    pinlayout['s_elevator'],
    elevator_atp(angle),
    0,0,0,0,0)


# Note to self: MAKE P AND S AILERON ALTERNATE IN SIGN FOR CORRECT FUNCTION
def set_aileron(m, angle):
    m.mav.command_long_send(
    m.target_system, m.target_component,
    mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
    0,
    pinlayout['p_aileron'],
    pflap_atp(-1*angle),
    0,0,0,0,0)
    
    m.mav.command_long_send(
    m.target_system, m.target_component,
    mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
    0,
    pinlayout['s_aileron'],
    sflap_atp(angle),
    0,0,0,0,0)


