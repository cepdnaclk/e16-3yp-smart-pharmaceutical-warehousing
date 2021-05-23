

#define interruptPin  3


#include "IR.h"
#include "STEPPER.h"
#include "arm.h"



STEPPER stepper;
ARM arm ;
IR ir ;


void setup() {
  Serial.begin(115200);
  pinMode(interruptPin, INPUT_PULLUP);

  delay(1000);
  attachInterrupt(digitalPinToInterrupt(interruptPin), limit_switch, LOW);

  // arm setup
  //stepper.setup();
  // calibration
 // stepper.calibration();
  arm.setup();

}


void limit_switch(){
  
  limit = true ;

}

void loop() {


  
}
