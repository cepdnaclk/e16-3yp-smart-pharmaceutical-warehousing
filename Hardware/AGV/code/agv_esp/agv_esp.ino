
#include <TaskScheduler.h>
#include <ESP8266WiFi.h> // Enables the ESP8266 to connect to the local network (via WiFi)
#include <PubSubClient.h> // Allows us to connect to, and publish to the MQTT broker


Scheduler ts; // scheduler event

char batteryPercentage = 80 ;

#include "display.h"
#include "battery.h"
#include "UART.h"
#include "MQTT.h"

Display  disp;
Battery battery;
UART uart ;
//MQTT mqtt ;



void mqttSubLoop();

#define PERIOD1 500
#define DURATION 10000

Task tBlink1 ( PERIOD1 * TASK_MILLISECOND, -1 , &mqttSubLoop, &ts, true );

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  uart.setup_disp(disp);
  battery.disp = disp ;
  mqtt.disp = disp ; 
  mqtt.qos = 3 ;
  mqtt.connection();

  //mqtt.pub();
  
}

void loop() {
  // put your main code here, to run repeatedly:
  
 // battery.reading();
  //uart.RX();
  ts.execute();

}

void mqttSubLoop(){
    mqtt.loop();
  
}
