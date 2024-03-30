#include <Wire.h>
#include "nutyperipheral.h"



void I2C_RequestHandler(void) {
  Serial.println("i2c message request, rxCounter: ");
  Serial.println(rxCounter, DEC);  
  
  attendRXMessage();

  //restart reception buffer
  rxCounter = 0;
}

void I2C_ReceiveHandler(int numBytesReceived) {
  Serial.print("i2c message received, ");
  Serial.println(numBytesReceived, DEC);  
  
  while (Wire1.available() > 0) {
    byte newReadByte = Wire1.read();
    if(rxCounter>=RXMAXLEN){
       Serial.println("i2c ignoring TOO MUCH DATA");
      continue;
    }
    rxData[rxCounter] = newReadByte;
    rxCounter++;
    Serial.print(" rxCounter: ");
    Serial.print(rxCounter, DEC);  
    Serial.println(".");
  }

}

void setup() {


  Serial.begin(115200);
  while (!Serial) {
    ;
  }
  nutyPeripheral.init(64, 1);
  Serial.println("run app :)");
  Wire1.setSDA(26);
  Wire1.setSCL(27);
  Wire1.begin(0x33);  // Initialize I2C (Slave Mode: address=0x55 )
  Wire1.onRequest(I2C_RequestHandler);
  Wire1.onReceive(I2C_ReceiveHandler);
  Serial.println("end setup");
}

int counter = 0;
void loop() {
  

  //Send response
  if( nutyPeripheral.responseLen >0 ){
      for(int r = 0; r<nutyPeripheral.responseLen; r++){
        Wire1.write(nutyPeripheral.response[r]);  
      }
      nutyPeripheral.responseLen = 0;
  }

  // Nothing To Be Done Here
  delay(1);
  counter ++;
  if(counter==3000){
    nutyPeripheral.statusReport = StatusReport::Rotary(2, false);
    counter = 0;
  }
}


