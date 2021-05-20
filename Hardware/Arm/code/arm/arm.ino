#include "IR.h"
#include "STEPPER.h"

IR ir ;
STEPPER stepper ;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  stepper.setup();
  stepper.loop();
  stepper.test();

}

void loop() {
  // put your main code here, to run repeatedly:
  //ir.read();
  //Serial.println(ir.analog);
  //delay(100);
  
}
