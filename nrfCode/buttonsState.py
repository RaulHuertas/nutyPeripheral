import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from keebAssignations import ButtonRegister
from keebAssignations import KeyAssignation
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


class ButtonsState :
    def __init__(self):
        self.buttonsAssignations =  [[ButtonRegister() for i in range(8)] for i in range(16)]
        self.assignFactory()
        self.kbd = Keyboard(usb_hid.devices)
    def buttonAssignation(self, row, column):
         return self.buttonsAssignations[row][column]
        
    def assignKeyCode(self, row, column, keycode):
        self.buttonAssignation(row,column).keyAssignation = KeyAssignation(KeyAssignation.CHARACTER)
        self.buttonAssignation(row,column).keyAssignation.keycode = keycode
        
    
    
    def assignFactory(self):
        self.assignKeyCode(1, 0, Keycode.Q)
        self.assignKeyCode(1, 7, Keycode.Y)
        
    def triggerKey(self, row, column, pressed):
        #print("trigger row: ", row)
        #print("trigger column: ", column)
        #print("trigger pressed: ", pressed)
        assignation = self.buttonAssignation(row, column)
        if assignation.isCharacter() :
            if pressed :
                #print("pressed ", assignation.keyAssignation.keycode)
                self.kbd.press(assignation.keyAssignation.keycode)
            else:
                #print("released ", assignation.keyAssignation.keycode)
                self.kbd.release(assignation.keyAssignation.keycode)

    



