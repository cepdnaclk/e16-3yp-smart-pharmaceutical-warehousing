
// 5 -  base motor( motor 1,2)
// 6 -  joint (motor 3)

// 9  -  risk (motor 4)
// 10  - griper (motor 5)
        
double static CX = 10 ;
double static CY = 100 ;


double static X = 100 ;
double static Y = 10 ;
    


#include <Servo.h>

class ARM{
  
  private:

  
    Servo servo_base;  // create servo object to control a servo
    Servo joint;
    Servo risk;
    Servo griper;
    // inital value 
    byte base_ag = 170 ;
    byte join_ag = 150 ;
    byte risk_ag =  50 ;
    byte grip_ag =  40 ;


    
    double alfa = 0 ;
    double beta = 0 ;
    double teta = 0 ;
    
    double r2 = 0 ;
    
    double tem = 0 ;
    
    int sigmoid_i = 0 ;
    
    double Calfa = 0 ;
    double Cbeta = 0 ;
        

    
  public :
  ARM(){

  }
  void setup(){
    servo_base.attach(5);  // attaches the servo on pin 9 to the servo object
    joint.attach(6);
    risk.attach(9);
    griper.attach(10);

    servo_base.write(base_ag);              // tell servo to go to position in variable 'pos'
    joint.write(join_ag);
    risk.write(risk_ag);
    griper.write(grip_ag);
  }

  void arm_move(){
    steps();
    KM();
    delay(20);
  }

  void steps(){

    double k = 1/(1+exp(-0.06*(sigmoid_i-75)));  
    sigmoid_i ++ ;
    CX = CX*(1-k)+X*k ;
    CY = CY*(1-k)+Y*k ;


   // overload();

  }

  void shutdown(){
     X = 50 ;
     Y = 50 ;
     
  }
  void disable(){
    servo_base.detach();
    joint.detach();
    risk.detach();
    griper.detach();
  }
  
  void down(){
      sigmoid_i = 0 ;
      griper.write(20);
      X = 100 ;
      Y = 10 ;
      
         
  }
  void up(){
    sigmoid_i = 0 ;
    griper.write(50);
    X = 10 ;
    Y = 180 ;
  }
  
  
  
  void  KM(){
      if ( (isnan(alfa)!= true ) && (isnan(beta)!= true) ) {
        Calfa = alfa *180 /PI ;
        Cbeta = beta * 180 / PI ;
      }
  
      tem = 90+Calfa;
      servo_base.write(tem);
      joint.write(90+Cbeta);
      risk.write(97+(Cbeta-Calfa));
      //gripper.write(0);
  
     /// X = map(analogRead(analogPin0),0,1023,0,200);  // read the input pin
     // Y = map(analogRead(analogPin1),0,1023,0,200);
  
      r2 = CX*CX + CY*CY ;
  
      tem = ((106*106+94*94)-r2)/(2*94*106) ; 
      
      beta = asin(tem);
      teta = atan((94*cos(beta))/(-94*sin(beta)+106));
  
      alfa = atan(CY/CX) + teta -PI/2 ;
    }
    

  
  
};
