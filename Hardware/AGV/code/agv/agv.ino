#include <Tasks.h>

byte val = 0 ;
String mqtt_in = "" ;
int sobel[10];    // ir sensor values

#include "SHIFT.h"
#include "IR.h"
#include "SONAR.h"
#include "UART.h"
#include "MOTION.h"

#include "CONTROL.h"

//SHIFT shift ;
Sonar sonar ;
UART uart;
MOTION motion ;


void irReadLoop();
void sonarLoop(void);

void blink(void) {
  digitalWrite(LED_BUILTIN,HIGH );
  delay(100);
  digitalWrite(LED_BUILTIN, LOW );
}


void setup() {
  //pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
  ir.shift = shift ;
  Tasks_Init();
  //Tasks_Add((Task)blink, 300, 0);
  Tasks_Add((Task) rx, 10, 0);
  Tasks_Add((Task) irReadLoop , 200 , 0);
  Tasks_Add((Task) sonarLoop, 200, 0);
  Tasks_Add((Task) FSM , 50 ,0 );
  Tasks_Start();
  
}

void loop() {
  
  

}


void irReadLoop(void){
  //ir.IR_read();
  ir.sobel_operator();
}

void sonarLoop(void){
  sonar.distance();
 
}

void rx(void){
  //Serial.println("kk");
  uart.RX();
}

void FSM(void){
  control.FSM();
}
