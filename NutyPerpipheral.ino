#include <Wire.h>
byte TxByte = 0xAA;

byte rxData[256];
int rxCounter = 0;

void I2C_RequestHandler(void) {
  Serial.println("i2c message request");
  Wire1.write('c');
  
  Wire1.write('d');
  rxCounter = 0;
}

void I2C_ReceiveHandler(int numBytesReceived) {
  Serial.print("i2c message received, ");
  Serial.println(numBytesReceived, DEC);
   while (Wire.available() > 0) {
     rxData[rxCounter] = Wire.read();
     rxCounter+++;
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


