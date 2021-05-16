class Sonar{
  private:
  public:
  // pingPin D12
  // eco D13
  
  
  char pingPin = 12;
  char echoPin    = 13;
  
  Sonar(){
    pinMode(pingPin,OUTPUT);
    pinMode(echoPin,INPUT);
    
  }
  void distance(){
       long duration, inches, cm;
       pinMode(pingPin, OUTPUT);
       digitalWrite(pingPin, LOW);
       delayMicroseconds(2);
       digitalWrite(pingPin, HIGH);
       delayMicroseconds(10);
       digitalWrite(pingPin, LOW);
       pinMode(echoPin, INPUT);
       duration = pulseIn(echoPin, HIGH);
       inches = microsecondsToInches(duration);
       cm = microsecondsToCentimeters(duration);
       Serial.print(inches);
       Serial.print("in, ");
       Serial.print(cm);
       Serial.print("cm");
       Serial.println();
       delay(100);
  }

  long microsecondsToInches(long microseconds) {
   return microseconds / 74 / 2;
  }
  
  long microsecondsToCentimeters(long microseconds) {
     return microseconds / 29 / 2;
  }
  
};
