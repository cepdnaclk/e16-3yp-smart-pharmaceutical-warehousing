#include <Servo.h>
#include <PID_v1.h>
#include <TaskScheduler.h>
#include <math.h>

#include "display.h"

#define dirPin 14
#define stepPin 16

double static CX = 10 ;
double static CY = 100 ;
double Z = 0 ;

double static X = 100 ;
double static Y = 10 ;


double alfa = 0 ;
double beta = 0 ;
double teta = 0 ;

double r2 = 0 ;

double tem = 0 ;

int sigmoid_i = 0 ;

double Calfa = 0 ;
double Cbeta = 0 ;

Servo servo_base;
Servo joint;
Servo risk;
Servo griper; 
  
Scheduler runner;


void steps();
void KM(); 

Task t1(40, TASK_FOREVER, &steps);

Task t2(20, TASK_FOREVER, &KM);

class SERVO_BASE {
  public:
    
  SERVO_BASE(){

    // set up servo
    servo_base.attach(13);
    joint.attach(15);
    risk.attach(3);
    griper.attach(1);   

    griper.write(20);

    lcdprint(0,"servo");

    pinMode(stepPin, OUTPUT);
    pinMode(dirPin, OUTPUT);

    // shedule

    runner.init();
    runner.addTask(t1);
    t1.enable();

    runner.addTask(t2);
    t2.enable();
         
  }

  void loop(){
    runner.execute();
  }


};

void overload();
void steps(){

    double k = 1/(1+exp(-0.06*(sigmoid_i-75)));  
    sigmoid_i ++ ;
    CX = CX*(1-k)+X*k ;
    CY = CY*(1-k)+Y*k ;

    lcdprint(0, "CX:"+String(int(CX))+"CY:"+String(int(CY))+"i:"+String(int(sigmoid_i)) );
    lcdprint(1,"X:"+String(int(X))+"\tY:"+String(int(Y)));

    overload();

  }

void overload(){
       if(sigmoid_i > 149 ){
       if(X > 98){     
        griper.write(50);
        X = 10 ;
        Y = 180 ;
        

       }else{
          griper.write(20);
          X = 100 ;
          Y = 10 ;
          
       }
       sigmoid_i = 0 ;
    }
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
