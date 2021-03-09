#include <TaskScheduler.h>
#include <PID_v1.h>


static char L_encoder = 0 ;
static char R_encoder = 0 ;
static char encoder  = 0 ;

static double CL_vel = 0 ;
static double CR_vel = 0 ;
static char C_velc = 0 ;

double Setpoint, LOutput , ROutput ;

int i = 0 ;

PID motorL(&CL_vel, &LOutput, &Setpoint,2,0.5,1, DIRECT);
PID motorR(&CR_vel, &ROutput, &Setpoint,2,0.5,1, DIRECT);

void velocity();
void street();
void leftturn();
void righturn();

Task t1(20 , TASK_FOREVER, &velocity);
Task t2(25 , 240 ,  &street);
Task t3(6000 , 1 ,  &leftturn);
Task t4(7000 , 1 ,  &righturn);

Scheduler runner;


class MOTOR
{
private:
    /* data */
    #define motort1IN1 4
    #define motort1IN2 7
    #define motort1PWM 6
    #define motort2IN2 8
    #define motort2IN1 9
    #define motort2PWM 5
    #define encoderR  3
    #define encoderL  2
    
    //Specify the links and initial tuning parameters
    

public:

    char MaxSpeed = 0 ;

    

    MOTOR() 
    {
        // setup pin out
        pinMode(motort1IN1,OUTPUT);
        pinMode(motort1IN2,OUTPUT);
        pinMode(motort1PWM,OUTPUT);
        pinMode(motort2IN1,OUTPUT);
        pinMode(motort2IN2,OUTPUT);
        pinMode(motort2PWM,OUTPUT);
        
        attachInterrupt(digitalPinToInterrupt(encoderL),Rencoder,RISING);  // interrupt
        attachInterrupt(digitalPinToInterrupt(encoderR),Lencoder,RISING); 

        runner.addTask(t1);
        runner.addTask(t2);

        t1.enable();
        t2.enable();

        Setpoint = 40;

        //turn the PID on
        motorL.SetMode(AUTOMATIC);
        motorR.SetMode(AUTOMATIC);
    }

    void loop(){
       runner.execute();
    }


    void static Lencoder(){
      L_encoder ++ ;
    }
    
    void static Rencoder(){
      R_encoder ++ ;
    }





 
};


void velocity(void){
      CL_vel = (CL_vel*19 )/20 + L_encoder ;
      CR_vel = (CR_vel*19 )/20 + R_encoder ;
      C_velc = (C_velc*19)/20 + encoder ;

      L_encoder = 0 ;
      R_encoder = 0 ;
      encoder = 0 ;
      
      //Serial.println(String(int(CL_vel)) +'\t'+LOutput +"\t"+String(int(CR_vel))+"\t"+ROutput);

}


void left(double speed_k){
    digitalWrite(motort1IN1,LOW);
    digitalWrite(motort1IN2,HIGH);
    analogWrite(motort1PWM,speed_k);
    
}

void  right(double speed_k){
    digitalWrite(motort2IN1,LOW);
    digitalWrite(motort2IN2,HIGH);
    analogWrite(motort2PWM,speed_k);
    
}

void leftturn(){
     motorL.Compute();
     left(LOutput);
     right(0);
}

void righturn(){
    
    motorR.Compute();
    right(ROutput);
    left(0);
}

void street(){
    Serial.println(i);
    i++;
     
     motorL.Compute();
     motorR.Compute();

     left(LOutput);
     
     right(ROutput);


}
