#include <AccelStepper.h>

bool limit = false ;
 
class STEPPER{
  //Dir A3
  //STEP A4

  #define dis_detw 8000 
  #define dirPin  A3
  #define stepPin A4
  #define motorInterfaceType 1
  #define max_length 400000 // max step
  #define slot_size 8000
  #define maxspeed 2000

  private:
    AccelStepper motor ;
  public:
  


  STEPPER(){
    
      
      motor = AccelStepper(motorInterfaceType, stepPin, dirPin);
      
  }

  void setup(){
    
    motor.setMaxSpeed(maxspeed);
  //  pinMode
  }

  void loop(){
      // Set the speed in steps per second:
      motor.setSpeed(maxspeed);
      // Step the motor with a constant speed as set by setSpeed():
      motor.runSpeed();
  }
  void left(){
      motor.setCurrentPosition(0);
    
      // Run the motor forward at 200 steps/second until the motor reaches 400 steps (2 revolutions):
      while(motor.currentPosition() < 3000)
      {
        motor.setSpeed(maxspeed);
        motor.runSpeed();
      }
    
      
    
      // Reset the position to 0:
      motor.setCurrentPosition(0);
    

  }
  void right(){
    
  }

  void calibration(){
    while(limit == false ){
      // move right until limit 
        motor.setSpeed(-maxspeed);
        motor.runSpeed();
      
    }

    motor.setCurrentPosition(0);
    
    
  }

  // slot to slot gap 14000 steps

 

  void move_slot(int k){
    
      if ( k * slot_size > max_length ){
        full_scale();
      }else if( k == 0 ){ // nagtive length ignore
        while(motor.currentPosition() < 1000  ) 
        {
            motor.setSpeed(maxspeed);
            motor.runSpeed();
        }
      }else{
        while(motor.currentPosition() < slot_size * k  ) 
        {
            motor.setSpeed(maxspeed);
            motor.runSpeed();
        }
      }
  }
  
  void full_scale(){
       while(motor.currentPosition() < max_length)
      {
        motor.setSpeed(maxspeed);
        motor.runSpeed();
      }
  }


};
