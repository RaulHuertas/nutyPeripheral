
#include "nutyperipheral.h"
#include <Wire.h>

byte rxData[RXMAXLEN];
int rxCounter = 0;


struct NutyPeripheralInfo nutyPeripheral;

void NutyPeripheralInfo::init(byte numberOfKeys, byte id){
  m_numberOfKeys = numberOfKeys;
  m_id = id;
  statusReport = StatusReport::None();
  
}

byte NutyPeripheralInfo::numberOfKeys()const{
  return m_numberOfKeys;
}

byte NutyPeripheralInfo::id()const{
  return m_id;
}

void attendRXMessage(){
  nutyPeripheral.responseLen = 0;
  //Serial.print("rxData[0]");
  //Serial.println(rxData[0], DEC);  
  if( (rxCounter == 1) && (rxData[0]==CMD_AREYOUNUTYDEVICE)){
    Serial.println("CMD_AREYOUNUTYDEVICE REQUEST");
    nutyPeripheral.response[0] = 'Y';
    nutyPeripheral.response[1] = 'E';
    nutyPeripheral.response[2] = 'S';
    nutyPeripheral.response[3] = nutyPeripheral.id();
    nutyPeripheral.response[4] = nutyPeripheral.numberOfKeys();
    nutyPeripheral.responseLen = 5;
  }
  else if( (rxCounter == 1) && (rxData[0]==CMD_STATUS)){
    //Serial.println("CMD_STATUS REQUEST");
    nutyPeripheral.response[0] = nutyPeripheral.statusReport.type;
    for(int j = 0; j<5; j++){
      nutyPeripheral.response[j+1] = nutyPeripheral.statusReport.params[j];
    }
    nutyPeripheral.statusReport = StatusReport::None();
    nutyPeripheral.responseLen = 6;
  }
 
}

