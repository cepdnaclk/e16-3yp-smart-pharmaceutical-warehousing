
#include <Servo.h>
#include "robotDefines.h"

String command;
String device;

// BT Module
#include <SoftwareSerial.h>
SoftwareSerial BT1(10, 11); // El pin 10 es Rx y el pin 11 es Tx

//---------------------------------------------
void setup() 
{
  
  Serial.begin(9600);
  BT1.begin(9600);
  
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
  
  // line follow sensors
  pinMode(lineFollowSensor0, INPUT);
  pinMode(lineFollowSensor1, INPUT);
  pinMode(lineFollowSensor2, INPUT);
  pinMode(lineFollowSensor3, INPUT);
  pinMode(lineFollowSensor4, INPUT);
  
  // servos
  leftServo.attach(5);
  rightServo.attach(3);
  
  BT1.print("MJRobot Line Follower is alive");
  BT1.println('\n');
  Serial.println("MJRobot Line Follower is alive ==> Presss the button to start");

  while (digitalRead(buttonPin))
  {  
  }
  
}

void loop() 
{
    readLFSsensors();    
    switch (mode)
  {
    case STOPPED: 
      motorStop();
      BT1.print("The End");
      ledBlink();
      previousError = error;
      break;

    case NO_LINE:  
      motorStop();
      motorTurn(LEFT, 180);
      previousError = 0;
      break;

    case FOLLOWING_LINE:     
      calculatePID();
      motorPIDcontrol();    
      break;     
  }
}


