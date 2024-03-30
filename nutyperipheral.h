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

enum RotaryEvent{
  INCREMENTED = 0,
  DECREASED = 1,
  PRESSED = 2,
  RELEASED = 3,
};

extern ButtonMatrix buttonsMatrix;
class StatusReport{
  public:
   StatusReportType type;
   byte params[5];
   static StatusReport None();
   static StatusReport KeyStroke(byte row, byte column, bool pressed);
   static StatusReport Rotary(byte index, RotaryEvent event);
   static StatusReport SliderValueChanged(byte index, uint32_t newValue);
};

template<typename T, int maxLen = 16> struct CircularBuffer{
  int start;
  int end;
  T buffer[maxLen];
  CircularBuffer(){
    start = 0;
    end = 0;
  }
  inline void clear(){
    start=end=0;
  }
  inline int capacity()const{
    return maxLen-1;
  }
  inline int length()const{
    return (end+maxLen-start)%maxLen;
  }
  inline bool full()const{
    return length()==capacity();
  }
  inline bool empty()const{
    return length()==0;
  }

  inline void addNew(const T& newElement){
    if(full()){
      return;
    }
    buffer[end] = newElement;
    end++;
    end%=maxLen;    
  }

  inline bool getOldest(T& oldestElement){
    if(empty()){
      return false;
    }
    oldestElement = buffer[start];
    start++;
    start%=maxLen;    
    return true;
  }


} ;

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
    CircularBuffer<StatusReport, 8> reports;
    //StatusReport statusReport;
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
