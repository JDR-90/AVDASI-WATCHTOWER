from TELEMETRY import *
from FC_CONNECT import *
from ANGLE_COMMAND import *
from FLAP_CONFIG import *
from time import sleep



m = connection_start(input("Kit number (7/8): "))
run_status_refresh(m)


while True:

    set_rudder(m, int(input("Rudder angle (-40 to 40): ")))
    set_elevator(m, int(input("Elevator angle (-45 to 45): ")))
    set_aileron(m, int(input("Aileron angle (-40 to 40): ")))
    set_flaps(m, int(input("Flap angle (0 to 30): ")))




    if input("Get servo data? (y/n): ") == 'y':
        data = get_SERVO_data
        for i in range (1,8):
            print(data[i])