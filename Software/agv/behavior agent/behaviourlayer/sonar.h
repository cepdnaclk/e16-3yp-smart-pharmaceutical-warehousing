#include <TaskScheduler.h>

#define echoPin D5 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin D4 //attach pin D3 Arduino to pin Trig of HC-SR04

long static duration; // variable for the duration of sound wave travel
int static distance; // variable for the distance measurement
    

long static timeout = 4000;
Scheduler runner;

void sonar_function();

Task t1(40, TASK_FOREVER, &sonar_function);

class Sonar{

  
  private:
    // defines variables


  public:
  Sonar(){  
     // 
      pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
      pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
      
      //Serial.println("Ultrasorunnernic Sensor HC-SR04 Test"); // print some text in Serial Monitor
      //Serial.println("with Arduino UNO R3");

      runner.init();
      runner.addTask(t1);
      t1.enable();
      
      
  }

  void loop(){
    runner.execute();
  }

};

  
void sonar_function(){
      // Clears the trigPin condition
      digitalWrite(trigPin, LOW);
      delayMicroseconds(2);
      // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
      digitalWrite(trigPin, HIGH);
      delayMicroseconds(10);
      digitalWrite(trigPin, LOW);
      // Reads the echoPin, returns the sound wave travel time in microseconds
      duration = pulseInLong(echoPin, HIGH,timeout);


      
      // Calculating the distance
      distance = (distance*0.7 + 0.3*duration * 0.034 / 2); // Speed of sound wave divided by 2 (go and back)
      // Displays the distance on the Serial Monitor

       if( duration == 0  ) {
        distance = 50 ;
      }
      printline( ("Dis: "+ String(distance) + "cm") , 1 );
      /*
      Serial.print("Distance: ");
      Serial.print(distance);
      Serial.print(" cm");
      Serial.print("Duration: ");
      Serial.print(duration);
      Serial.println(" us");*/
      delay(100);
  }
