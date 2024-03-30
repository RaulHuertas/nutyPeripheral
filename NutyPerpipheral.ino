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

  Serial.println("run app :)");
  Wire1.setSDA(26);
  Wire1.setSCL(27);
  Wire1.begin(0x33);  // Initialize I2C (Slave Mode: address=0x55 )
  Wire1.onRequest(I2C_RequestHandler);
  Wire1.onReceive(I2C_ReceiveHandler);
  Serial.println("end setup");
}

void loop() {
  // Nothing To Be Done Here
  delay(1);
}


