import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from keebAssignations import ButtonRegister

class ButtonsState :
    def __init__(self):
        self.buttonsAssignations =  [[ButtonRegister() for i in range(8)] for i in range(16)]

    def buttonAssignation(self, row, column):
         return self.buttonsAssignations[row][column]

    def triggerKey(self, row, column, pressed):
        print("trigger row: ", row)
        print("trigger column: ", column)
        print("trigger pressed: ", pressed)
        pass





