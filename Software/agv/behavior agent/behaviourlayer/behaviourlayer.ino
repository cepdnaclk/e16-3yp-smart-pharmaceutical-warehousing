#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#include "display.h"
#include "sonar.h"
#include "battery.h"
#include "UART.h"
#include <TaskScheduler.h>

Sonar sonar ;
Battery battery ;
UART uart;


void setup() {
  LCD();
  delay(1000);
  //Serial.begin(9600); // // Serial Communication is starting with 9600 of baudrate speed
 // Serial1.begin(115200);
  pinMode(4,OUTPUT);

}
void loop() {
  sonar.loop();
  battery.loop();
  //uart.loop();
  //Serial.println("kji");
  //delay(500);
 
}
