#include <Wire.h>
#include "nutyperipheral.h"

const int FirstColumn = 12;
const int FirstRow = 18;

void I2C_RequestHandler(void) {
  //Serial.println("i2c message request, rxCounter: ");
  //Serial.println(rxCounter, DEC);  
  
  attendRXMessage();

  //restart reception buffer
  rxCounter = 0;
}

void I2C_ReceiveHandler(int numBytesReceived) {
  //Serial.print("i2c message received, ");
  //Serial.println(numBytesReceived, DEC);  
  
  while (Wire1.available() > 0) {
    byte newReadByte = Wire1.read();
    if(rxCounter>=RXMAXLEN){
       //Serial.println("i2c ignoring TOO MUCH DATA");
      continue;
    }
    rxData[rxCounter] = newReadByte;
    rxCounter++;
    //Serial.print(" rxCounter: ");
    //Serial.print(rxCounter, DEC);  
    //Serial.println(".");
  }

}

void setup() {


  //Serial.begin(115200);
  //while (!Serial) {
  //  ;
  //}
  pinMode(LED_BUILTIN, OUTPUT);

  nutyPeripheral.init(64, 1);
  //Serial.println("run app :)");
  //SETUP COMMUNICTION WITH MASTER
  Wire1.setSDA(26);
  Wire1.setSCL(27);
  Wire1.begin(0x33); 
  Wire1.onRequest(I2C_RequestHandler);
  Wire1.onReceive(I2C_ReceiveHandler);
  //SETUP SCANNING
  for(int column = 0; column<6; column++){
    int columnPinNMumber = FirstColumn+column;
    pinMode(columnPinNMumber, OUTPUT);          
    digitalWrite(columnPinNMumber, LOW);      
  }
  for(int row = 0; row<6; row++){
    int rowPinNMumber = FirstRow+row;
    pinMode(rowPinNMumber, INPUT_PULLUP);     
    
  }
  




  //Serial.println("end setup");



}

const int maxCounter = 50;

int counter = 0;
void loop() {
  counter++;
  if(counter<maxCounter/2){
     digitalWrite(LED_BUILTIN, HIGH);
  }else{
     digitalWrite(LED_BUILTIN, LOW);
  }
  counter%=maxCounter;
  //SEND RESPONSE
  if( nutyPeripheral.responseLen >0 ){
      for(int r = 0; r<nutyPeripheral.responseLen; r++){
        Wire1.write(nutyPeripheral.response[r]);  
      }
      nutyPeripheral.responseLen = 0;
  }

  //SCAN  
  for (int c = 0; c < 6; c++)
  {
        
        for(int columnPin = 0; columnPin<6; columnPin++){
          if(columnPin==c){
            digitalWrite(FirstColumn+columnPin, LOW);
          }else{
            digitalWrite(FirstColumn+columnPin, HIGH);
          }
        }
        
        delay(5);
        for (int r = 0; r < 6; r++)
        {

            uint8_t estadoRow = digitalRead(FirstRow+r);
            bool isPressed = (estadoRow == 0);
            if(nutyPeripheral.buttonsMatrix.button(r,c).pressed!=isPressed){              
              nutyPeripheral.reports.addNew( StatusReport::KeyStroke(r, c, isPressed) );
              nutyPeripheral.buttonsMatrix.button(r,c).pressed=isPressed;
              // if(isPressed){
              //   Serial.print("Pressed: ");
              // }else{
              //   Serial.print("Released: ");
              // }
              // Serial.print("row ");
              // Serial.print(r);
              // Serial.print(", column ");
              // Serial.println(c);
            }
            
        }
  }

  delay(1);
  
  // counter ++;
  // if(counter==3000){
  //   nutyPeripheral.statusReport = StatusReport::Rotary(2, false);
  //   counter = 0;
  // }
}


