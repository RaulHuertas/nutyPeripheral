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
        self.mediaConsumerControl = ConsumerControl(usb_hid.devices)
        self.shiftPressed = False
        self.altGrPressed = False
        self.mouseMode = False
        self.fnMode = False

    def buttonAssignation(self, row, column):
         return self.buttonsAssignations[row][column]
        
    def assignKeyCode(self, row, column, keycode, fnKeyCode = None):
        if keycode!=None :
            self.buttonAssignation(row,column).keyAssignation = KeyAssignation(KeyAssignation.CHARACTER)
            self.buttonAssignation(row,column).keyAssignation.keycode = keycode
        
        if fnKeyCode!=None :
           self.buttonAssignation(row,column).keyFnAssignation.keycode = fnKeyCode
        
    def assignMedia(self, row, column, consumerControlCode):
        self.buttonAssignation(row,column).keyAssignation = KeyAssignation(KeyAssignation.MEDIA)
        self.buttonAssignation(row,column).mediaConsumerControlCode = consumerControlCode
        
        
    def assignAsFn(self, row, column):
        self.buttonAssignation(row,column).keyAssignation = KeyAssignation(KeyAssignation.FN)
        
    def assignAsMouseModeActivator(self, row, column):
        self.buttonAssignation(row,column).keyAssignation = KeyAssignation(KeyAssignation.MOUSE_MODE)
    def assignAsLayerSettings(self, row, column):
        self.buttonAssignation(row,column).keyAssignation = KeyAssignation(KeyAssignation.LAYER_OR_SETTINGS)        
        
            
    
    def assignFactory(self):
        #numbers top row
        self.assignKeyCode(0, 0, Keycode.ONE, Keycode.F1)
        self.assignKeyCode(0, 1, Keycode.TWO, Keycode.F2)
        self.assignKeyCode(0, 2, Keycode.THREE, Keycode.F3)
        self.assignKeyCode(0, 3, Keycode.FOUR, Keycode.F4)
        self.assignKeyCode(0, 4, Keycode.FIVE, Keycode.F5)
        self.assignKeyCode(0, 5, None, Keycode.F11)      
        
        self.assignKeyCode(0, 6, None, Keycode.F12)      
        self.assignKeyCode(0, 7, Keycode.SIX, Keycode.F6)
        self.assignKeyCode(0, 8, Keycode.SEVEN, Keycode.F7)
        self.assignKeyCode(0, 9, Keycode.EIGHT, Keycode.F8)
        self.assignKeyCode(0, 10, Keycode.NINE, Keycode.F9)
        self.assignKeyCode(0, 11, Keycode.ZERO, Keycode.F10)
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
        self.assignAsMouseModeActivator(2, 5)  
        
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
        self.assignAsLayerSettings(3, 5)   
        
        self.assignKeyCode(3, 7, Keycode.N)
        self.assignKeyCode(3, 8, Keycode.M)
        self.assignKeyCode(3, 9, Keycode.COMMA)
        self.assignKeyCode(3, 10, Keycode.PERIOD)
        self.assignKeyCode(3, 11, Keycode.FORWARD_SLASH)
        
        #modifiers row
        self.assignKeyCode(4, 0, Keycode.CONTROL)
        self.assignKeyCode(4, 1, Keycode.ALT)
        self.assignKeyCode(4, 2, Keycode.WINDOWS)
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
        self.assignMedia(5, 0, ConsumerControlCode.VOLUME_DECREMENT)
        self.assignMedia(5, 1, ConsumerControlCode.MUTE)
        self.assignMedia(5, 2, ConsumerControlCode.VOLUME_INCREMENT)
        self.assignKeyCode(5, 3, Keycode.SHIFT)
        self.assignAsFn(5, 4)
        self.assignKeyCode(5, 5, Keycode.MINUS)
        
        self.assignKeyCode(5, 6, Keycode.ESCAPE)
        self.assignKeyCode(5, 7, Keycode.APPLICATION)
        self.assignKeyCode(5, 8, Keycode.GUI)
        self.assignKeyCode(5, 9, Keycode.LEFT_ARROW)
        self.assignKeyCode(5, 10, Keycode.DOWN_ARROW)
        self.assignKeyCode(5, 11, Keycode.RIGHT_ARROW)
        
    def trigerFnFunction(self, row, column, pressed):
        assignation = self.buttonAssignation(row, column)
        if assignation.keyAssignation.selection == KeyAssignation.NONE :
            return
        if assignation.keyFnAssignation.keycode == None :
            return;
        
        if pressed :
            self.kbd.press(assignation.keyFnAssignation.keycode)
        else:
            self.kbd.release(assignation.keyFnAssignation.keycode)
            
    def triggerKey(self, row, column, pressed):
        #print("trigger row: ", row)
        #print("trigger column: ", column)
        #print("trigger pressed: ", pressed)
        assignation = self.buttonAssignation(row, column)
        if assignation.isCharacter() :
            if self.fnMode:
                self.trigerFnFunction(row, column, pressed)
            else :
                if pressed :
                    #print("pressed ", assignation.keyAssignation.keycode)
                    self.kbd.press(assignation.keyAssignation.keycode)
                else:
                    #print("released ", assignation.keyAssignation.keycode)
                    self.kbd.release(assignation.keyAssignation.keycode)
        elif assignation.isMediaKey():
            if pressed :
                self.mediaConsumerControl.press(assignation.mediaConsumerControlCode)
            else:
                self.mediaConsumerControl.release()
        elif assignation.isMouseModeEnabler():
            self.mouseMode = pressed
        elif assignation.isFn():
            self.fnMode = pressed


