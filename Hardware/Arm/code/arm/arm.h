
// 10 - base motor
// 9 - 1 joint

// 6  - 3 join
// 5  - griper

#include <Servo.h>

class ARM{
  
  private:
    Servo shoulder0;  // create servo object to control a servo
    Servo shoulder1;
    Servo join;
    Servo risk;
    Servo gripper;
  public :
  ARM(){

  }
  void setup(){
    shoulder0.attach(10);  // attaches the servo on pin 9 to the servo object
    shoulder1.attach(9);
    join.attach(6);
    risk.attach(5);

    shoulder0.write(90);              // tell servo to go to position in variable 'pos'
    shoulder1.write(90);
    join.write(90);
    risk.write(90);
  }

  
  
};
