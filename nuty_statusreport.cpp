#include "nutyperipheral.h"
#include <Wire.h>

StatusReport StatusReport::None(){
  StatusReport ret;
  ret.type = StatusReportType::NONE;
  for(int j = 0; j<5; j++){
    ret.params[j] = 0;
  }
  return ret;
}

StatusReport StatusReport::KeyStroke(byte row, byte column, bool pressed){
  StatusReport ret;
  ret.type = StatusReportType::KEY_STROKE;
  for(int j = 0; j<5; j++){
    ret.params[j] = 0;
  }
  ret.params[0] = row;
  ret.params[1] = column;
  ret.params[2] = pressed;
  return ret;
}

StatusReport StatusReport::Rotary(byte index, bool incremented){
  StatusReport ret;
  ret.type = StatusReportType::ROTARY;
  for(int j = 0; j<5; j++){
    ret.params[j] = 0;
  }
  ret.params[0] = index;
  ret.params[1] = incremented;
  return ret;
}

StatusReport StatusReport::SliderValueChanged(byte index, uint32_t newValue){
  StatusReport ret;
  ret.type = StatusReportType::SLIDER_VALUE_CHANGED;
  for(int j = 0; j<5; j++){
    ret.params[j] = 0;
  }
  ret.params[0] = index;
  ret.params[1] = newValue;
  return ret;
}








