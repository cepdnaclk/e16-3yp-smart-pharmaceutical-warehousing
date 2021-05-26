#include <Tasks.h>
#include <PID_v1.h>

byte val = 0 ;
String mqtt_in = "" ;
int IR_arr[12];    // ir sensor values

 // encoder pin 2,3


#include "SHIFT.h"
#include "IR.h"
#include "SONAR.h"
#include "UART.h"
#include "MOTION.h"

#include "CONTROL.h"

//SHIFT shift ;
//IR ir ;
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

  Serial.begin(115200);
  ir.shift = shift ;

  
  Tasks_Init();
  //Tasks_Add((Task)blink, 300, 0);
  Tasks_Add((Task) rx, 10, 0);
  //Tasks_Add((Task) irReadLoop , 200 , 0);
  Tasks_Add((Task) sonarLoop, 200, 0);
  Tasks_Add((Task) FSM , 50 ,0 );
  Tasks_Start();
  
}

void loop() {

  //motion.vel_left();
  /*
  ir.IR_read();
  delay(100);*/
 // interrupt_left_encoder();

  

}



void irReadLoop(void){
  ir.IR_read();
  //ir.sobel_operator();
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
