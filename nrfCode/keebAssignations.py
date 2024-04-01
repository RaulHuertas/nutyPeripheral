import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

class MouseAction (object):
    NONE = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    LEFT_CLICK = 5
    RIGHT_CLICK = 6
    SCROLL_UP = 7
    SCROLL_DOWN = 8
    SCROLL_CLICK = 9
    DETAIL_MOVEMENT = 10
    def __init__( self, newVal ):
        if newVal in ( self.NONE,
                       self.UP,
                       self.DOWN ,
                       self.LEFT,
                       self.RIGHT,
                       self.LEFT_CLICK,
                       self.RIGHT_CLICK,
                       self.SCROLL_UP,
                       self.SCROLL_DOWN,
                       self.SCROLL_CLICK,
                       self.DETAIL_MOVEMENT
                       ):            
            self.selection= newVal
        else :
            self.selection= self.NONE



class KeyAssignation(object):
    NONE = 0
    CHARACTER = 1
    MEDIA = 2
    FN = 3
    MOUSE_MODE = 4
    MOUSE_CODE = 5
    MIDI = 6
    LAYER_OR_SETTINGS = 7
    def __init__( self, newVal ):
        self.keycode = None
        self.mediaConsumerControlCode = None
        self.midiCode = None
        self.mouseCode = None
        if newVal in ( self.NONE, self.CHARACTER, self.MEDIA , self.FN, self.MOUSE_MODE, self.MIDI, self.LAYER_OR_SETTINGS):            
            self.selection= newVal
        else :
            self.selection= self.NONE
            

class ButtonRegister :
    def __init__(self):
        self.lastTimePressed = 0;
        self.lastTimeReleased = 0;
        self.lastTimePressed_prev = 0;
        self.lastTimeReleased_prev = 0;
        self.m_lastUpdateTime = 0;
        self.pressedNow = False;
        self.m_hasChanged = False;
        self.keyAssignation = KeyAssignation(KeyAssignation.NONE)
        self.keyFnAssignation = KeyAssignation(KeyAssignation.NONE) #triggered when Fn is pressed
        self.mouseAction =  MouseAction(MouseAction.NONE)
        #self.mediaConsumerControlCode =
    def isCharacter(self):
        return self.keyAssignation.selection == KeyAssignation.CHARACTER
    def isShift(self):
        if not self.isCharacter() :
            return False
        return self.keyAssignation.keyCode == KeyCode.SHIFT
    def isAlt(self):
        if not self.isCharacter() :
            return False
        return self.keyAssignation.keyCode == KeyCode.ALT
    def isAltGr(self):
        if not self.isCharacter() :
            return False
        return self.keyAssignation.keyCode == KeyCode.RIGHT_ALT
    def isFn(self):        
        return self.keyAssignation.selection == KeyAssignation.FN
    def isLayerOrSettings(self):        
        return self.keyAssignation.selection == KeyAssignation.LAYER_OR_SETTINGS
    def isMouseModeEnabler(self):        
        return self.keyAssignation.selection == KeyAssignation.MOUSE_MODE
    def isMIDI(self):        
        return self.keyAssignation.selection == KeyAssignation.MIDI
    def isMediaKey(self):        
        return self.keyAssignation.selection == KeyAssignation.MEDIA
        
class MouseState :
    def __init__(self):
        self.movingUp = False
        self.movingDown = False
        self.movingLeft = False
        self.movingRight = False
