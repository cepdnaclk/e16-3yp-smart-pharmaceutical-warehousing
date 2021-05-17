#include <Tasks.h>


#include "SHIFT.h"
#include "IR.h"
#include "SONAR.h"
#include "UART.h"

IR ir ;
SHIFT shift ;
Sonar sonar ;
UART uart;


void irReadLoop();
void sonarLoop();

void setup() {

  Serial.begin(115200);
  ir.shift = shift ;
  Tasks_Init();
  Tasks_Add();
}

void loop() {
  // put your main code here, to run repeatedly:
  //delay(1000);
  
  //sonar.distance();
  //shift.set( 0b00011000 , 0b00001000 );
  //uart.TX();
  
}

void irReadLoop(){
  ir.IR_read();
}

void sonarLoop(){
  sonar.distance();
  delay(200);
}
