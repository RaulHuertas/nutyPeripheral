#ifndef NUTYPERIPHERALHPP
#define NUTYPERIPHERALHPP

#include <Arduino.h>
#include "nutykeeb.h"
#define RXMAXLEN 256

enum StatusReportType{
  NONE = 0, 
  KEY_STROKE = 1, 
  ROTARY = 2, 
  SLIDER_VALUE_CHANGED = 3
};
extern ButtonMatrix buttonsMatrix;
class StatusReport{
  public:
   StatusReportType type;
   byte params[5];
   static StatusReport None();
   static StatusReport KeyStroke(byte row, byte column, bool pressed);
   static StatusReport Rotary(byte index, bool incremented);
   static StatusReport SliderValueChanged(byte index, uint32_t newValue);
};

class NutyPeripheralInfo{
  private:
    byte m_numberOfKeys;
    byte m_id;

  public:
    void init(byte numberOfKeys, byte id);
    byte numberOfKeys()const;
    byte id()const;    
    byte response[6];
    byte responseLen = 0;
    StatusReport statusReport;
    ButtonMatrix buttonsMatrix;
};
extern byte rxData[RXMAXLEN];
extern int rxCounter;
extern struct NutyPeripheralInfo nutyPeripheral;

#define CMD_AREYOUNUTYDEVICE 0x01U
#define CMD_STATUS 0x02U
#define CMD_UPDATE_LEDS 0x03U

void attendRXMessage();

#endif //NUTYPERIPHERALHPP
