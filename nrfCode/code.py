import busio
from board import *
import board
import time
from adafruit_bus_device.i2c_device import I2CDevice
import nutyPeripheral

A_DEVICE_REGISTER = 0x0E  # device id register on the DS3231 board
leftSide = nutyPeripheral.NutyPeripheral();

with busio.I2C(board.A5, board.A4) as i2c:
    device = I2CDevice(i2c, 0x33)
    bytes_read = bytearray(1)
    
    with device as bus_device:
        leftSide.init(bus_device)
            
    while True :
        with device as bus_device:
            leftSide.getStatus(bus_device)
                
        time.sleep(0.020)