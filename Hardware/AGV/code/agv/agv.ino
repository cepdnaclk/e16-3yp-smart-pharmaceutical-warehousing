

#include "IR.h"
#include "SHIFT.h"
#include "SONAR.h"
#include "UART.h"

IR ir ;
SHIFT shift ;
Sonar sonar ;
UART uart;

void setup() {

  Serial.begin(115200);

  
}

void loop() {
  // put your main code here, to run repeatedly:
  //delay(1000);
  //ir.IR_read();
  //sonar.distance();
  shift.set( 0b00011000 , 0b00001000 );
  uart.TX();
  
}
