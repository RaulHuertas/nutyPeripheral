from adafruit_bus_device.i2c_device import I2CDevice
from adafruit_mcp230xx.mcp23017 import MCP23017
import time
import digitalio
import keebAssignations
CMD_AREYOUNUTYDEVICE = 1
CMD_STATUS = 2
 
TYPECODE_NONE = 0
TYPECODE_KEY_STROKE = 1
TYPECODE_ROTARY = 2
TYPECODE_SLIDER_VALUE_CHANGED = 3
class NutyPeripheralBase :
     def __init__(self):
         self.rowOffset = 0;
         self.columnOffset = 0;
         self.buttonsState = None
         #self.startTime =   time.monotonic()
         
class NutyPeripheral(NutyPeripheralBase):
    id = 0
    nKeys = 0
    
    def __init__(self):
        super().__init__()
        
    def init(self, bus_device):
        bytesToWrite = bytearray(1)
        bytesToWrite[0] = CMD_AREYOUNUTYDEVICE
        bus_device.write(bytesToWrite)
        
        result = bytearray(5)
        ret = False;
        try :
            bus_device.readinto(result)
            id = result[3]
            nKeys = result[4]
            #print("id read: ", id)
            #print("nKeys read", nKeys)
            ret = True
        except:
            #print("error reading i2c")
            pass
            
        #print(result)
        return ret

    def getStatus(self, bus_device):
        bytesToWrite = bytearray(1)
        bytesToWrite[0] = CMD_STATUS
        bus_device.write(bytesToWrite)
        result = bytearray(6)
        ret = False;
        #now = time.monotonic()
       
        
        try :
            bus_device.readinto(result)
            ret = True  
        except:
                print("error reading i2c")
        if not ret :
            return
            
        typeCodeReceived = result[0]
           
        if typeCodeReceived == TYPECODE_NONE:
            #print("TYPECODE_NONE RECEIVED")
            pass
        elif typeCodeReceived == TYPECODE_KEY_STROKE:
            #print("TYPECODE_KEY_STROKE RECEIVED")
            row = result[1]
            column = result[2]
            pressed = result[3]
            #print("row: ", row)
            #print("column: ", column)
            #print("pressed: ", pressed)
            self.buttonsState.triggerKey(
                row+self.rowOffset,
                column+self.columnOffset,
                pressed!=0
            )    
        elif typeCodeReceived == TYPECODE_ROTARY:
            print("TYPECODE_ROTARY RECEIVED")
        elif typeCodeReceived == TYPECODE_SLIDER_VALUE_CHANGED:
            print("TYPECODE_SLIDER_VALUE_CHANGED RECEIVED")   
        #print(result)
        return ret

class NutyMCPPeripheral(NutyPeripheralBase):
    mcp = None
    
    def __init__(self, i2cBus):
        super().__init__()
        self.mcp = MCP23017(i2cBus)
        self.buttonsMatrix =  [[False for i in range(6)] for i in range(6)]
        self.columnsPin = [None for i in range(6)]
        self.rowsPin = [None for i in range(6)]
        self.columnsPin[0] = self.mcp.get_pin(2)
        self.columnsPin[1] = self.mcp.get_pin(3)
        self.columnsPin[2] = self.mcp.get_pin(4)
        self.columnsPin[3] = self.mcp.get_pin(5)
        self.columnsPin[4] = self.mcp.get_pin(6)
        self.columnsPin[5] = self.mcp.get_pin(7)
        self.rowsPin[0] = self.mcp.get_pin(8)
        self.rowsPin[1] = self.mcp.get_pin(9)
        self.rowsPin[2] = self.mcp.get_pin(10)
        self.rowsPin[3] = self.mcp.get_pin(11)
        self.rowsPin[4] = self.mcp.get_pin(12)
        self.rowsPin[5] = self.mcp.get_pin(13)
        
        for col in self.columnsPin :
            col.direction = digitalio.Direction.OUTPUT                
            col.value = False
            
        for row in self.rowsPin :
            row.direction = digitalio.Direction.INPUT                
            row.pull  = digitalio.Pull.UP    
            
    def getStatus(self):                
    
        c = 0
        while c < 6: # per column
            columnPin = 0
            while columnPin < 6:
                if columnPin==c : 
                    self.columnsPin[columnPin].value  = False
                else :
                    self.columnsPin[columnPin].value  = True
                columnPin += 1
            #time.sleep(0.001)            
                
            r = 0
            while r < 6:#per row
                currentlyPressed = (self.rowsPin[r].value == False);
                if self.buttonsMatrix[r][c] !=  currentlyPressed:
                    #print("Cambio de estado row: ", r)
                    #print("Cambio de estado column: ", c)
                    self.buttonsMatrix[r][c] = currentlyPressed
                    self.buttonsState.triggerKey(
                        r+self.rowOffset,
                        c+self.columnOffset,
                        currentlyPressed
                    )
                r += 1#end of per row
                
            c+=1 # end of per column
            
                
            
                
