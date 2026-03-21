from pymavlink import mavutil

def get_flap_angle(connection):
    # Wait specifically for NAMED_VALUE_FLOAT
    msg = connection.recv_match(type='NAMED_VALUE_FLOAT', blocking=False)
    
    # Clean the string (MAVLink strings are null-terminated)
    if msg is not None:
        sensor_name = msg.name.strip('\x00')
    
        if sensor_name == "AS5600":
            return msg.value
    return None
