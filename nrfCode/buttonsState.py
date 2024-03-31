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
        self.buttonsAssignations =  [[ButtonRegister() for i in range(16)] for i in range(16)]
        self.assignFactory()
        self.kbd = Keyboard(usb_hid.devices)
    def buttonAssignation(self, row, column):
         return self.buttonsAssignations[row][column]
        
    def assignKeyCode(self, row, column, keycode):
        self.buttonAssignation(row,column).keyAssignation = KeyAssignation(KeyAssignation.CHARACTER)
        self.buttonAssignation(row,column).keyAssignation.keycode = keycode
        
    def assignAsFn(self, row, column):
        self.buttonAssignation(row,column).keyAssignation = KeyAssignation(KeyAssignation.FN)
    
    def assignFactory(self):
        #characters top row
        self.assignKeyCode(1, 0, Keycode.Q)
        self.assignKeyCode(1, 1, Keycode.W)
        self.assignKeyCode(1, 2, Keycode.E)
        self.assignKeyCode(1, 3, Keycode.R)
        self.assignKeyCode(1, 4, Keycode.T)        
        
        self.assignKeyCode(1, 7, Keycode.Y)
        self.assignKeyCode(1, 8, Keycode.U)
        self.assignKeyCode(1, 9, Keycode.I)
        self.assignKeyCode(1, 10, Keycode.O)
        self.assignKeyCode(1, 11, Keycode.P)
        #characters home row
        self.assignKeyCode(2, 0, Keycode.A)
        self.assignKeyCode(2, 1, Keycode.S)
        self.assignKeyCode(2, 2, Keycode.D)
        self.assignKeyCode(2, 3, Keycode.F)
        self.assignKeyCode(2, 4, Keycode.G)        
        
        self.assignKeyCode(2, 7, Keycode.H)
        self.assignKeyCode(2, 8, Keycode.J)
        self.assignKeyCode(2, 9, Keycode.K)
        self.assignKeyCode(2, 10, Keycode.L)
        self.assignKeyCode(2, 11, Keycode.SEMICOLON)
        
        #characters bottom row
        self.assignKeyCode(3, 0, Keycode.Z)
        self.assignKeyCode(3, 1, Keycode.X)
        self.assignKeyCode(3, 2, Keycode.C)
        self.assignKeyCode(3, 3, Keycode.V)
        self.assignKeyCode(3, 4, Keycode.B)        
        
        self.assignKeyCode(3, 7, Keycode.N)
        self.assignKeyCode(3, 8, Keycode.M)
        self.assignKeyCode(3, 9, Keycode.COMMA)
        self.assignKeyCode(3, 10, Keycode.PERIOD)
        self.assignKeyCode(3, 11, Keycode.FORWARD_SLASH)
        
        #space
        self.assignKeyCode(4, 3, Keycode.SPACE)
        #enter
        self.assignKeyCode(4, 8, Keycode.ENTER)
        
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

    



