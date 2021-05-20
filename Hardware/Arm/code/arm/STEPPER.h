#include <AccelStepper.h>

class STEPPER{
  //Dir A3
  //STEP A4

  #define dirPin  A3
  #define stepPin A4
  #define motorInterfaceType 1
  
  private:
    AccelStepper stepper ;
  public:

  STEPPER(){
      stepper = AccelStepper(motorInterfaceType, stepPin, dirPin);
  }

  void setup(){
    stepper.setMaxSpeed(1000);
  }

  void loop(){
      // Set the speed in steps per second:
      stepper.setSpeed(400);
      // Step the motor with a constant speed as set by setSpeed():
      stepper.runSpeed();
  }
  void test(){
      stepper.setCurrentPosition(0);
    
      // Run the motor forward at 200 steps/second until the motor reaches 400 steps (2 revolutions):
      while(stepper.currentPosition() > -9000)
      {
        stepper.setSpeed(-3200);
        stepper.runSpeed();
      }

  }
  
};
