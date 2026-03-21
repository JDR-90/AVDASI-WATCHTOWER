from math import degrees
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



def get_ATTITUDE(m):

    """
    Function to get the pitch, roll, yaw position from the vehicle.
    Returns the variable in degrees.
    """


    # sending message to request attitude data
    msg = m.recv_match(type='ATTITUDE', blocking=True, timeout=1)



    # if no data in message
    if msg is None:
        print('no data received')
        return None
    
    # if data in message
    else:
        pitch = round(degrees(msg.pitch),2)
        roll = round(degrees(msg.roll), 2)
        yaw = round(degrees(msg.yaw), 2)
        return pitch, roll, yaw



def get_SERVO_data(m):

    ServoData = [0,0,0,0,0,0,0]
    msg = m.recv_match(type='SERVO_OUTPUT_RAW', blocking=True, timeout=2)

    # if no data in message
    if msg is None:
        return ServoData


    
    else:
        # if data in message
        ServoData = [getattr(msg, f'servo{pos}_raw') for pos in range (1,8)]

        # Convert PWM to angle based on servo position
        ServoData[0] = pflap_pta(ServoData[0])
        ServoData[1] = pflap_pta(ServoData[1])
        ServoData[2] = sflap_pta(ServoData[2])
        ServoData[3] = sflap_pta(ServoData[3])
        ServoData[4] = rudder_pta(ServoData[4])
        ServoData[5] = elevator_pta(ServoData[5])
        ServoData[6] = elevator_pta(ServoData[6])


        return ServoData
        
