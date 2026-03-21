from machine import I2C, Pin
import time

AS5600_ADDR = 0x36
RAW_ANGLE_H = 0x0C
RAW_ANGLE_L = 0x0D

class AS5600:
    def __init__(self, i2c):
        self.i2c = i2c

    def read_raw(self):
        high = self.i2c.readfrom_mem(AS5600_ADDR, RAW_ANGLE_H, 1)[0]
        low = self.i2c.readfrom_mem(AS5600_ADDR, RAW_ANGLE_L, 1)[0]
        return ((high << 8) | low) & 0x0FFF

    def read_deg(self):
        return self.read_raw() * 360 / 4096

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
sensor = AS5600(i2c)

while True:
    print(sensor.read_deg())
    time.sleep(0.2)

