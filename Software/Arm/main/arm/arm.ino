#include <ESP8266WiFi.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#include "servo.h"


SERVO_BASE servo ;

void setup() {
 // Serial.begin(115200);
  pinMode(D4,OUTPUT);
  digitalWrite(D4,LOW);  

  
  lcd_setup();
  lcdprint(0,"praveen");
}

void loop() {
 // 

 //Serial.println("kkkkkkkkkkkk");
 
  
 servo.loop();  
 //colour.loop();
 

}
