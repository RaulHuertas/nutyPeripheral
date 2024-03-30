from adafruit_bus_device.i2c_device import I2CDevice

CMD_AREYOUNUTYDEVICE = 1
CMD_STATUS = 2
 
TYPECODE_NONE = 0
TYPECODE_KEY_STROKE = 1
TYPECODE_ROTARY = 2
TYPECODE_SLIDER_VALUE_CHANGED = 3

class NutyPeripheral:
    id = 0
    nKeys = 0
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
            print("id read: ", id)
            print("nKeys read", nKeys)
            ret = True
        except:
            print("error reading i2c")
            
        print(result)
        return ret

    def getStatus(self, bus_device):
        bytesToWrite = bytearray(1)
        bytesToWrite[0] = CMD_STATUS
        bus_device.write(bytesToWrite)
        result = bytearray(6)
        ret = False;
        try :
            bus_device.readinto(result)
            ret = True
            typeCodeReceived = result[0]
           
            if typeCodeReceived == TYPECODE_NONE:
                #print("TYPECODE_NONE RECEIVED")
                pass
            elif typeCodeReceived == TYPECODE_KEY_STROKE:
                print("TYPECODE_KEY_STROKE RECEIVED")
                row = result[1]
                column = result[2]
                pressed = result[3]
                print("row: ", row)
                print("column: ", column)
                print("pressed: ", pressed)
            elif typeCodeReceived == TYPECODE_ROTARY:
                print("TYPECODE_ROTARY RECEIVED")
            elif typeCodeReceived == TYPECODE_SLIDER_VALUE_CHANGED:
                print("TYPECODE_SLIDER_VALUE_CHANGED RECEIVED")                
        except:
                print("error reading i2c")
            
        #print(result)
        return ret
        
