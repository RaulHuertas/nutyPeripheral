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
        #numbers top row
        self.assignKeyCode(0, 0, Keycode.ONE)
        self.assignKeyCode(0, 1, Keycode.TWO)
        self.assignKeyCode(0, 2, Keycode.THREE)
        self.assignKeyCode(0, 3, Keycode.FOUR)
        self.assignKeyCode(0, 4, Keycode.FIVE)        
        
        self.assignKeyCode(0, 7, Keycode.SIX)
        self.assignKeyCode(0, 8, Keycode.SEVEN)
        self.assignKeyCode(0, 9, Keycode.EIGHT)
        self.assignKeyCode(0, 10, Keycode.NINE)
        self.assignKeyCode(0, 11, Keycode.ZERO)
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
        
        #modifiers row
        self.assignKeyCode(4, 0, Keycode.CONTROL)
        self.assignKeyCode(4, 1, Keycode.ALT)
        self.assignKeyCode(4, 2, Keycode.GUI)
        self.assignKeyCode(4, 3, Keycode.SPACE)
        self.assignKeyCode(4, 4, Keycode.TAB)
        self.assignKeyCode(4, 5, Keycode.BACKSPACE)
        
        self.assignKeyCode(4, 6, Keycode.DELETE)
        self.assignKeyCode(4, 7, Keycode.RIGHT_ALT)
        self.assignKeyCode(4, 8, Keycode.ENTER)
        self.assignKeyCode(4, 9, Keycode.PRINT_SCREEN)
        self.assignKeyCode(4, 10, Keycode.UP_ARROW)
        self.assignKeyCode(4, 11, Keycode.PAUSE)
        
        #Modifiers bottom row
        #self.assignKeyCode(5, 0, Keycode.CONTROL)
        #self.assignKeyCode(5, 1, Keycode.ALT)
        #self.assignKeyCode(5, 2, Keycode.GUI)
        self.assignKeyCode(5, 3, Keycode.SHIFT)
        #self.assignKeyCode(5, 4, Keycode.TAB)
        self.assignKeyCode(5, 5, Keycode.FORWARD_SLASH)
        
        self.assignKeyCode(5, 6, Keycode.ESCAPE)
        self.assignKeyCode(5, 7, Keycode.APPLICATION)
        #self.assignKeyCode(5, 8, Keycode.ENTER)
        self.assignKeyCode(5, 9, Keycode.LEFT_ARROW)
        self.assignKeyCode(5, 10, Keycode.DOWN_ARROW)
        self.assignKeyCode(5, 11, Keycode.RIGHT_ARROW)
        
        
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

    



