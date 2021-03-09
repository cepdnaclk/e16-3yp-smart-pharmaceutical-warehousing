/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/


// 11 - base motor
// 10 - 1 joint
// 9  - 2 joint
// 6  - 3 join
// 5  - griper

#include <Servo.h>

Servo shoulder0;  // create servo object to control a servo
Servo shoulder1;
Servo join;
Servo risk;
Servo gripper;
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position


int analogPin0 = A0;
int analogPin1 = A1;
int analogPin2 = A2;
int analogPin3 = A3;

int val0 = 0 ;
int val1 = 0 ;
int val2 = 0 ;
int val3 = 0 ;

double X = 0;
double Y = 0;

double alfa = 0 ;
double beta = 0 ;
double teta = 0 ;

double r2 = 0 ;

double tem = 0 ;


double Calfa = 0 ;
double Cbeta = 0 ;

void setup() {

  Serial.begin(9600);           //  setup serial
  
  shoulder0.attach(11);  // attaches the servo on pin 9 to the servo object
  shoulder1.attach(10);
  join.attach(9);
  risk.attach(6);
  //gripper.attach(5);
}

void loop() {

    if ( (isnan(alfa)!= true ) && (isnan(beta)!= true) ) {
      Calfa = alfa *180 /PI ;
      Cbeta = beta * 180 / PI ;
    }

    tem = 90+Calfa;
    shoulder0.write(tem);              // tell servo to go to position in variable 'pos'
    shoulder1.write(tem);
    join.write(90+Cbeta);
    risk.write(97+(Cbeta-Calfa));
    //gripper.write(0);

    X = map(analogRead(analogPin0),0,1023,0,200);  // read the input pin
    Y = map(analogRead(analogPin1),0,1023,0,200);

    r2 = X*X + Y*Y ;

    tem = ((106*106+94*94)-r2)/(2*94*106) ; 
    
    beta = asin(tem);
    teta = atan((94*cos(beta))/(-94*sin(beta)+106));

    alfa = atan(Y/X) + teta -PI/2 ;

   
    Serial.print(X);
    Serial.print("\t");
    Serial.print(Y);
    Serial.print("\t");
    Serial.print(alfa*180/PI);
    Serial.print("\t");
    Serial.println(beta*180/PI);
    delay(40);
}
