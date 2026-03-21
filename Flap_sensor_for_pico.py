from machine import I2C, Pin, UART
import struct
import time

# ==================================================
# MAVLink v1 constants
# ==================================================
MAVLINK_STX = 0xFE

SYS_ID = 1                  # External sensor ID
COMP_ID = 10                 # MAV_COMP_ID_PERIPHERAL

MSG_ID_HEARTBEAT = 0
MSG_ID_NAMED_VALUE_FLOAT = 251

CRC_EXTRA_HEARTBEAT = 50
CRC_EXTRA_NAMED_VALUE_FLOAT = 170

MAV_TYPE_GENERIC = 0
MAV_AUTOPILOT_INVALID = 8
MAV_MODE_MANUAL_ARMED = 64
MAV_STATE_ACTIVE = 4

_mav_seq = 0


# ==================================================
# CRC (X25)
# ==================================================
def x25_crc(buf):
    crc = 0xFFFF
    for b in buf:
        tmp = b ^ (crc & 0xFF)
        tmp = (tmp ^ (tmp << 4)) & 0xFF
        crc = ((crc >> 8)^ (tmp << 8)^ (tmp << 3)^ (tmp >> 4)) & 0xFFFF
    return crc


# ==================================================
# MAVLink packet sender (v1)
# ==================================================
def mavlink_send(uart, msg_id, payload, crc_extra):
    global _mav_seq

    length = len(payload)

    header = struct.pack("<BBBBBB",MAVLINK_STX,length,_mav_seq,SYS_ID,COMP_ID,msg_id)

    crc_input = header[1:] + payload + bytes([crc_extra])
    crc = x25_crc(crc_input)

    packet = header + payload + struct.pack("<H", crc)
    
    

    uart.write(packet)
    _mav_seq = (_mav_seq + 1) & 0xFF


# ==================================================
# HEARTBEAT message
# ==================================================
def mavlink_heartbeat(uart):
    payload = struct.pack("<IBBBBB",0,MAV_TYPE_GENERIC,MAV_AUTOPILOT_INVALID,MAV_MODE_MANUAL_ARMED,MAV_STATE_ACTIVE,3)
    mavlink_send(uart, MSG_ID_HEARTBEAT, payload, CRC_EXTRA_HEARTBEAT)


# ==================================================
# NAMED_VALUE_FLOAT message
# ==================================================
def mavlink_named_value_float(uart, name, value):
    
    name_bytes = (name.encode("ascii") + b'\x00' * 10)[:10]

    payload = struct.pack("<I10sf",time.ticks_ms() & 0xFFFFFFFF,name_bytes,float(value))
    
    mavlink_send(uart, MSG_ID_NAMED_VALUE_FLOAT, payload, CRC_EXTRA_NAMED_VALUE_FLOAT)


# ==================================================
# AS5600 Hall Sensor
# ==================================================
AS5600_ADDR = 0x36
RAW_ANGLE_H = 0x0C


class AS5600:
    def __init__(self, i2c):
        self.i2c = i2c

    def read_deg(self):
        data = self.i2c.readfrom_mem(AS5600_ADDR, RAW_ANGLE_H, 2)
        raw = ((data[0] << 8) | data[1]) & 0x0FFF
        return raw * 360.0 / 4096.0


# ==================================================
# Hardware setup
# ==================================================
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=100000)
sensor = AS5600(i2c)

uart = UART(0,baudrate=115200,tx=Pin(0),rx=Pin(1))



def hexdump(b):
    return ' '.join('{:02X}'.format(x) for x in b)



# ==================================================
# Main loop
# ==================================================
last_hb = 0

while True:
    now = time.ticks_ms()

    # Send heartbeat at 1 Hz
    if time.ticks_diff(now, last_hb) >= 1000:
        mavlink_heartbeat(uart)
        last_hb = now

    try:
        angle = sensor.read_deg()
        mavlink_named_value_float(uart, "AS5600", angle)
        print("Angle:", angle)
    except OSError as e:
        print("I2C error:", e)

    time.sleep(0.2)   # 5 Hz data rate
    
    
    
    


