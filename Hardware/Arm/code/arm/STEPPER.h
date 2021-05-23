#include <AccelStepper.h>

bool limit = false ;
 
class STEPPER{
  //Dir A3
  //STEP A4

  #define dis_detw 8000 
  #define dirPin  A3
  #define stepPin A4
  #define motorInterfaceType 1
  

  private:
    AccelStepper motor ;
  public:
  


  STEPPER(){
    
      
      motor = AccelStepper(motorInterfaceType, stepPin, dirPin);
      
  }

  void setup(){
    
    motor.setMaxSpeed(1000);
  //  pinMode
  }

  void loop(){
      // Set the speed in steps per second:
      motor.setSpeed(400);
      // Step the motor with a constant speed as set by setSpeed():
      motor.runSpeed();
  }
  void left(){
      motor.setCurrentPosition(0);
    
      // Run the motor forward at 200 steps/second until the motor reaches 400 steps (2 revolutions):
      while(motor.currentPosition() < 3000)
      {
        motor.setSpeed(3200);
        motor.runSpeed();
      }
    
      
    
      // Reset the position to 0:
      motor.setCurrentPosition(0);
    
      // Run the motor backwards at 600 steps/second until the motor reaches -200 steps (1 revolution):
      while(motor.currentPosition() > -3000) 
      {

      }
  }
  void right(){
    
  }

  void calibration(){
    while(limit == false ){
      // move right until limit 
        motor.setSpeed(-3200);
        motor.runSpeed();
      
    }

    motor.setCurrentPosition(0);
    
    
  }

  void full_scale(){
       while(motor.currentPosition() < 40000)
      {
        motor.setSpeed(3200);
        motor.runSpeed();
      }
  }


};
