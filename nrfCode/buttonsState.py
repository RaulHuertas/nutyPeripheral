import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from keebAssignations import ButtonRegister
from keebAssignations import KeyAssignation
from keebAssignations import MouseAction
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

class MouseState :
    def __init__(self):
        self.movingUp = False
        self.movingDown = False
        self.movingLeft = False
        self.movingRight = False
        self.enabled = False
        self.detailMoveEnabled = False

class ButtonsState :
    def __init__(self):
        self.buttonsAssignations =  [[ButtonRegister() for i in range(16)] for i in range(16)]
        self.assignFactory()
        self.kbd = Keyboard(usb_hid.devices)
        self.mediaConsumerControl = ConsumerControl(usb_hid.devices)
        self.mouse = Mouse(usb_hid.devices)
        self.shiftPressed = False
        self.altGrPressed = False        
        self.mouseState = MouseState();
        self.fnMode = False
        


    def buttonAssignation(self, row, column):
         return self.buttonsAssignations[row][column]
        
    def assignKeyCode(self, row, column, keycode, fnKeyAssignation = KeyAssignation.NONE, fnCode = None):
        if keycode!=None :
            self.buttonAssignation(row,column).keyAssignation = KeyAssignation(KeyAssignation.CHARACTER)
            self.buttonAssignation(row,column).keyAssignation.keycode = keycode
        
        if fnKeyAssignation==KeyAssignation.CHARACTER :
           self.buttonAssignation(row,column).keyFnAssignation = KeyAssignation(KeyAssignation.CHARACTER)
           self.buttonAssignation(row,column).keyFnAssignation.keycode = fnCode
           #print("fn function assigned")
        elif fnKeyAssignation==KeyAssignation.MEDIA :
           self.buttonAssignation(row,column).keyFnAssignation = KeyAssignation(KeyAssignation.MEDIA)
           self.buttonAssignation(row,column).keyFnAssignation.mediaConsumerControlCode = fnCode        
        
    def assignMouseModeFunction(self, row, column, mouseActionCode = MouseAction.NONE):
        assignation = self.buttonAssignation(row, column)
        assignation.mouseAction =  MouseAction(mouseActionCode)
        
        
    def assignMedia(self, row, column, consumerControlCode, fnKeyAssignation = KeyAssignation.NONE, fnCode = None):
        self.buttonAssignation(row,column).keyAssignation = KeyAssignation(KeyAssignation.MEDIA)
        self.buttonAssignation(row,column).keyAssignation.mediaConsumerControlCode = consumerControlCode
        if fnKeyAssignation==KeyAssignation.CHARACTER :
           self.buttonAssignation(row,column).keyFnAssignation = KeyAssignation(KeyAssignation.CHARACTER)
           self.buttonAssignation(row,column).keyFnAssignation.keycode = fnCode
           #print("fn function assigned")
        elif fnKeyAssignation==KeyAssignation.MEDIA :
           self.buttonAssignation(row,column).keyFnAssignation = KeyAssignation(KeyAssignation.MEDIA)
           self.buttonAssignation(row,column).keyFnAssignation.mediaConsumerControlCode = fnCode   
        
        
    def assignAsFn(self, row, column):
        self.buttonAssignation(row,column).keyAssignation = KeyAssignation(KeyAssignation.FN)
        
    def assignAsMouseModeActivator(self, row, column):
        self.buttonAssignation(row,column).keyAssignation = KeyAssignation(KeyAssignation.MOUSE_MODE)
        
    def assignAsLayerSettings(self, row, column):
        self.buttonAssignation(row,column).keyAssignation = KeyAssignation(KeyAssignation.LAYER_OR_SETTINGS)        
        
            
    
    def assignFactory(self):
        #numbers top row
        self.assignKeyCode(0, 0, Keycode.ONE, KeyAssignation.CHARACTER, Keycode.F1)
        self.assignKeyCode(0, 1, Keycode.TWO, KeyAssignation.CHARACTER, Keycode.F2)
        self.assignKeyCode(0, 2, Keycode.THREE, KeyAssignation.CHARACTER, Keycode.F3)
        self.assignKeyCode(0, 3, Keycode.FOUR, KeyAssignation.CHARACTER, Keycode.F4)
        self.assignKeyCode(0, 4, Keycode.FIVE, KeyAssignation.CHARACTER, Keycode.F5)
        self.assignKeyCode(0, 5, None, KeyAssignation.CHARACTER, Keycode.F11)      
        
        self.assignKeyCode(0, 6, None, KeyAssignation.CHARACTER, Keycode.F12)      
        self.assignKeyCode(0, 7, Keycode.SIX, KeyAssignation.CHARACTER, Keycode.F6)
        self.assignKeyCode(0, 8, Keycode.SEVEN, KeyAssignation.CHARACTER, Keycode.F7)
        self.assignKeyCode(0, 9, Keycode.EIGHT, KeyAssignation.CHARACTER, Keycode.F8)
        self.assignKeyCode(0, 10, Keycode.NINE, KeyAssignation.CHARACTER, Keycode.F9)
        self.assignKeyCode(0, 11, Keycode.ZERO, KeyAssignation.CHARACTER, Keycode.F10)
        #characters top row
        self.assignKeyCode(1, 0, Keycode.Q)
        self.assignKeyCode(1, 1, Keycode.W)
        self.assignKeyCode(1, 2, Keycode.E)
        self.assignKeyCode(1, 3, Keycode.R)
        self.assignKeyCode(1, 4, Keycode.T)        
        
        self.assignKeyCode(1, 6, Keycode.LEFT_BRACKET)
        self.assignKeyCode(1, 7, Keycode.Y);self.assignMouseModeFunction(1, 7, MouseAction.SCROLL_UP); 
        self.assignKeyCode(1, 8, Keycode.U); self.assignMouseModeFunction(1, 8, MouseAction.LEFT_CLICK)
        self.assignKeyCode(1, 9, Keycode.I); self.assignMouseModeFunction(1, 9, MouseAction.UP)
        self.assignKeyCode(1, 10, Keycode.O); self.assignMouseModeFunction(1, 10, MouseAction.RIGHT_CLICK)
        self.assignKeyCode(1, 11, Keycode.P)
        #characters home row
        self.assignKeyCode(2, 0, Keycode.A)
        self.assignKeyCode(2, 1, Keycode.S)
        self.assignKeyCode(2, 2, Keycode.D)
        self.assignKeyCode(2, 3, Keycode.F)
        self.assignKeyCode(2, 4, Keycode.G); self.assignMouseModeFunction(2, 4, MouseAction.DETAIL_MOVEMENT)
        self.assignAsMouseModeActivator(2, 5)  
        
        self.assignKeyCode(2, 6, Keycode.RIGHT_BRACKET, KeyAssignation.CHARACTER, Keycode.KEYPAD_PLUS )
        self.assignKeyCode(2, 7, Keycode.H, KeyAssignation.CHARACTER, Keycode.KEYPAD_MINUS ); self.assignMouseModeFunction(2, 7, MouseAction.SCROLL_DOWN)
        self.assignKeyCode(2, 8, Keycode.J, KeyAssignation.CHARACTER, Keycode.KEYPAD_ASTERISK ); self.assignMouseModeFunction(2, 8, MouseAction.LEFT)
        self.assignKeyCode(2, 9, Keycode.K, KeyAssignation.CHARACTER, Keycode.KEYPAD_FORWARD_SLASH ); self.assignMouseModeFunction(2, 9, MouseAction.DOWN)
        self.assignKeyCode(2, 10, Keycode.L); self.assignMouseModeFunction(2, 10, MouseAction.RIGHT)
        self.assignKeyCode(2, 11, Keycode.SEMICOLON)
        
        #characters bottom row
        self.assignKeyCode(3, 0, Keycode.Z)
        self.assignKeyCode(3, 1, Keycode.X)
        self.assignKeyCode(3, 2, Keycode.C)
        self.assignKeyCode(3, 3, Keycode.V)
        self.assignKeyCode(3, 4, Keycode.B)
        self.assignAsLayerSettings(3, 5)   
        
        self.assignKeyCode(3, 6, Keycode.GRAVE_ACCENT)
        self.assignKeyCode(3, 7, Keycode.N);self.assignMouseModeFunction(3, 7, MouseAction.SCROLL_CLICK)
        self.assignKeyCode(3, 8, Keycode.M)
        self.assignKeyCode(3, 9, Keycode.COMMA, KeyAssignation.CHARACTER, Keycode.KEYPAD_ENTER  )
        self.assignKeyCode(3, 10, Keycode.PERIOD)
        self.assignKeyCode(3, 11, Keycode.FORWARD_SLASH)
        
        #modifiers row
        self.assignKeyCode(4, 0, Keycode.CONTROL, KeyAssignation.MEDIA, ConsumerControlCode.BRIGHTNESS_DECREMENT)
        self.assignKeyCode(4, 1, Keycode.ALT, KeyAssignation.MEDIA, ConsumerControlCode.STOP)
        self.assignKeyCode(4, 2, Keycode.WINDOWS, KeyAssignation.MEDIA, ConsumerControlCode.BRIGHTNESS_INCREMENT)
        self.assignKeyCode(4, 3, Keycode.SPACE)
        self.assignKeyCode(4, 4, Keycode.TAB)
        self.assignAsFn(4, 5)
        
        self.assignKeyCode(4, 6, Keycode.DELETE)
        self.assignKeyCode(4, 7, Keycode.RIGHT_ALT)
        self.assignKeyCode(4, 8, Keycode.ENTER)
        self.assignKeyCode(4, 9, Keycode.PRINT_SCREEN)
        self.assignKeyCode(4, 10, Keycode.UP_ARROW)
        self.assignKeyCode(4, 11, Keycode.PAUSE)
        
        #Modifiers bottom row
        self.assignMedia(5, 0, ConsumerControlCode.VOLUME_DECREMENT	, KeyAssignation.MEDIA, ConsumerControlCode.SCAN_PREVIOUS_TRACK)
        self.assignMedia(5, 1, ConsumerControlCode.MUTE				, KeyAssignation.MEDIA, ConsumerControlCode.PLAY_PAUSE)
        self.assignMedia(5, 2, ConsumerControlCode.VOLUME_INCREMENT	, KeyAssignation.MEDIA, ConsumerControlCode.SCAN_NEXT_TRACK)
        self.assignKeyCode(5, 3, Keycode.SHIFT)
        self.assignKeyCode(5, 4, Keycode.BACKSPACE)
        self.assignKeyCode(5, 5, Keycode.MINUS)
        
        self.assignKeyCode(5, 6, Keycode.ESCAPE)
        self.assignKeyCode(5, 7, Keycode.APPLICATION)
        self.assignKeyCode(5, 8, Keycode.GUI)
        self.assignKeyCode(5, 9, Keycode.LEFT_ARROW)
        self.assignKeyCode(5, 10, Keycode.DOWN_ARROW)
        self.assignKeyCode(5, 11, Keycode.RIGHT_ARROW)
        
    def triggerCharacter(self, keycode, pressed):
        #print("triggerCharacter")
        if pressed :
            self.kbd.press(keycode)
        else:            
            self.kbd.release(keycode)
            
    def triggerMediaCode(self, ccCode, pressed):
        if pressed :
            self.mediaConsumerControl.press(ccCode)
        else:
            self.mediaConsumerControl.release()
    def triggerFnFunction(self, row, column, pressed):
        assignation = self.buttonAssignation(row, column)               
        if assignation.keyFnAssignation.selection == KeyAssignation.CHARACTER :
            self.triggerCharacter(assignation.keyFnAssignation.keycode, pressed);
        elif assignation.keyFnAssignation.selection == KeyAssignation.MEDIA :
            self.triggerMediaCode(assignation.keyFnAssignation.mediaConsumerControlCode, pressed);
    
    def triggerMouseFunction(self, row, column, pressed):
        assignation = self.buttonAssignation(row, column)
        if assignation.mouseAction.selection == MouseAction.NONE :
            return
        elif assignation.mouseAction.selection == MouseAction.LEFT_CLICK :
            if pressed :
                self.mouse.press(Mouse.LEFT_BUTTON)
            else:
                self.mouse.release(Mouse.LEFT_BUTTON)
        elif assignation.mouseAction.selection == MouseAction.RIGHT_CLICK :
            if pressed :
                self.mouse.press(Mouse.RIGHT_BUTTON)
            else:
                self.mouse.release(Mouse.RIGHT_BUTTON)
        elif assignation.mouseAction.selection == MouseAction.SCROLL_CLICK :
            if pressed :
                self.mouse.press(Mouse.MIDDLE_BUTTON )
            else:
                self.mouse.release(Mouse.MIDDLE_BUTTON )
        elif assignation.mouseAction.selection == MouseAction.SCROLL_UP :
            if pressed :
                self.mouse.move(wheel = 1 )
        elif assignation.mouseAction.selection == MouseAction.SCROLL_DOWN :
            if pressed :
                self.mouse.move(wheel = -1 )
        elif assignation.mouseAction.selection == MouseAction.DETAIL_MOVEMENT :
                self.mouseState.detailMoveEnabled = pressed
        elif assignation.mouseAction.selection == MouseAction.UP :
                self.mouseState.movingUp = pressed
        elif assignation.mouseAction.selection == MouseAction.DOWN :
                self.mouseState.movingDown = pressed
        elif assignation.mouseAction.selection == MouseAction.LEFT :
                self.mouseState.movingLeft = pressed
        elif assignation.mouseAction.selection == MouseAction.RIGHT :
                self.mouseState.movingRight = pressed
               
    def evaluateStatus(self):
        #check mouse status
        if self.mouseState.enabled:
            normalMove = 10
            detailMove = 1
            dx = 0
            dy = 0
            if self.mouseState.movingLeft :
                dx -= (detailMove if self.mouseState.detailMoveEnabled else normalMove)
            if self.mouseState.movingRight :
                dx += (detailMove if self.mouseState.detailMoveEnabled else normalMove)
            if self.mouseState.movingUp :
                dy -= (detailMove if self.mouseState.detailMoveEnabled else normalMove)
            if self.mouseState.movingDown :
                dy += (detailMove if self.mouseState.detailMoveEnabled else normalMove)
            
            if (dx!=0) or (dy!=0) :
                self.mouse.move(x=dx, y=dy )
        pass
    
    def triggerKey(self, row, column, pressed):
        #print("trigger row: ", row)
        #print("trigger column: ", column)
        #print("trigger pressed: ", pressed)
        assignation = self.buttonAssignation(row, column)
        #print("assignation.keyAssignation.selection: ", assignation.keyAssignation.selection)
        if self.fnMode and not assignation.isFn():
            #print("fn enabler")
            self.triggerFnFunction(row, column, pressed)
        elif self.mouseState.enabled and not assignation.isMouseModeEnabler():
            #print("mouse enabler")
            self.triggerMouseFunction(row, column, pressed)        
        elif assignation.isCharacter():
            #print("assignation.isCharacter()")
            self.triggerCharacter(assignation.keyAssignation.keycode, pressed)
        elif assignation.isMediaKey():
            #print("assignation.isMediaKey()")
            self.triggerMediaCode(assignation.keyAssignation.mediaConsumerControlCode,pressed)            
        elif assignation.isMouseModeEnabler():
            #print("assignation.isMouseModeEnabler()")
            self.mouseState.enabled = pressed
        elif assignation.isFn():            
            self.fnMode = pressed
            #print("assignation.isFn(): ", self.fnMode )


