
#define interruptPin  3


//#include "IR.h"
#include "STEPPER.h"
#include "arm.h"



STEPPER stepper;
ARM arm ;
//IR ir ;


void setup() {
  Serial.begin(115200);
  pinMode(interruptPin, INPUT_PULLUP);
  
  delay(1000);
  attachInterrupt(digitalPinToInterrupt(interruptPin), limit_switch, LOW);
  arm.setup();
  delay(1000);
  // arm setup
  stepper.setup();
  // calibration
  stepper.calibration();
  delay(500);
  stepper.move_slot(0); 
  
  delay(1000);
  arm.down();
  arm_move();
  delay(1000);
  arm.up();
  arm_move();
  delay(1000);
  
  
  stepper.move_slot(1);  //move to slot
  delay(500);
  arm.down();
  arm_move();
  delay(1000);
  arm.up();
  arm_move();
  delay(1000);

  stepper.move_slot(2);  //move to slot
  delay(500);
  arm.down();
  arm_move();
  delay(1000);
  arm.up();
  arm_move();
  delay(1000);

  stepper.move_slot(3);  //move to slot
  delay(500);
  arm.down();
  arm_move();
  delay(1000);
  arm.up();
  arm_move();
  delay(1000);

  
  arm.shutdown();
  arm_move();
  delay(1000);
  arm.disable();

}


void limit_switch(){
  
  limit = true ;

}

void loop() {
    
  
  
}
void arm_move(){
  for(byte i = 0 ; i < 150 ; i++ ){
    arm.arm_move();
  }
}
