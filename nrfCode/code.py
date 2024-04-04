import busio
from board import *
import board
import time
from adafruit_bus_device.i2c_device import I2CDevice
import nutyPeripheral
import keebAssignations
import buttonsState
from digitalio import DigitalInOut, Direction, Pull

A_DEVICE_REGISTER = 0x0E  # device id register on the DS3231 board
led = DigitalInOut(board.LED_BLUE)
led.direction = Direction.OUTPUT

led.value= False
#print(dir(nutyPeripheral))
buttonsState = buttonsState.ButtonsState()
i2cBus = None
deviceLeft = None
leftSide = nutyPeripheral.NutyPeripheral()
#Connect to left sid5e
i2cBus = busio.I2C(board.A5, board.A4, frequency=800_000) 
deviceLeft = I2CDevice(i2cBus, 0x33)
leftSide.rowOffset = 0
leftSide.columnOffset = 0
leftSide.buttonsState = buttonsState
with deviceLeft as bus_device:
    leftSide.init(bus_device)
rightSideMCP = nutyPeripheral.NutyMCPPeripheral(i2cBus)
rightSideMCP.rowOffset = 0
rightSideMCP.columnOffset = 6
rightSideMCP.buttonsState = buttonsState
#main loop            
while True :
    #print(deviceLeft)
    #check left side events
    if deviceLeft != None :
        with deviceLeft as bus_device :
            leftSide.getStatus(bus_device)
    rightSideMCP.getStatus()
    buttonsState.evaluateStatus()
    time.sleep(0.001)
