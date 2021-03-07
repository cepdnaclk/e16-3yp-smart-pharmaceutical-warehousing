#include <Tasks.h>
#include <PID_v1.h>


static char L_encoder = 0 ;
static char R_encoder = 0 ;
static char encoder  = 0 ;

static double CL_vel = 0 ;
static double CR_vel = 0 ;
static char C_velc = 0 ;

double Setpoint, LOutput , ROutput ;

PID motorL(&CL_vel, &LOutput, &Setpoint,2,0.1,1, DIRECT);
PID motorR(&CR_vel, &ROutput, &Setpoint,2,5,1, DIRECT);


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
        
        attachInterrupt(digitalPinToInterrupt(encoderL),Lencoder,RISING);  // interrupt
        attachInterrupt(digitalPinToInterrupt(encoderR),Rencoder,RISING); 

        Tasks_Init();
        Tasks_Add((Task) velocity, 200, 0);
        Tasks_Add((Task) street, 25, 0);
        Tasks_Start();


        Setpoint = 20;

        //turn the PID on
        motorL.SetMode(AUTOMATIC);
        motorR.SetMode(AUTOMATIC);
    }

    static void left(double speed_k){
        digitalWrite(motort1IN1,LOW);
        digitalWrite(motort1IN2,HIGH);
        analogWrite(motort1PWM,speed_k);
        
    }

   static void  right(double speed_k){
        digitalWrite(motort2IN1,LOW);
        digitalWrite(motort2IN2,HIGH);
        analogWrite(motort2PWM,speed_k);
        
    }

    void static Lencoder(){
      L_encoder ++ ;
    }
    
    void static Rencoder(){
      R_encoder ++ ;
    }


     static void velocity(void){
          CL_vel = L_encoder ;
          CR_vel = R_encoder ;
          C_velc = encoder ;

          L_encoder = 0 ;
          R_encoder = 0 ;
          encoder = 0 ;
          
          Serial.println(String(int(CL_vel)) +'\t'+LOutput +"\t"+String(int(CR_vel))+"\t"+String(int(C_velc)));

    }

    static void street(){
         
         motorL.Compute();
        // motorR.Compute();

         left(LOutput);
         //right(ROutput);
 
  
    }


 
};
