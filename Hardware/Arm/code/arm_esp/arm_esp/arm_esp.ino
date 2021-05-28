
#include <TaskScheduler.h>
#include <ESP8266WiFi.h> // Enables the ESP8266 to connect to the local network (via WiFi)
#include <PubSubClient.h> // Allows us to connect to, and publish to the MQTT broker


Scheduler ts; // scheduler event

String batteryPercentage = "80" ;
String IP = "";

#include "display.h"
Display  disp;
#include "battery.h"
#include "MQTT.h"
#include "UART.h"



Battery battery;
UART uart ;
//MQTT mqtt ;



void mqttSubLoop();

#define PERIOD1 500
#define DURATION 10000

Task tmqtt ( PERIOD1 * TASK_MILLISECOND, -1 , &mqttSubLoop, &ts, true );

void batteryLevel();
Task tbatt ( 60000 * TASK_MILLISECOND, -1 , &batteryLevel, &ts, true );

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  uart.setup_disp(disp);
  battery.disp = disp ;
 // mqtt.disp = disp ; 
  mqtt.qos = 3 ;
  mqtt.connection();
  battery.reading();

  

  
}

void loop() {
  // put your main code here, to run repeatedly:
  
 // 
  //uart.RX();
  ts.execute();

}

void mqttSubLoop(){
    mqtt.loop();
  
}

void batteryLevel(){
    battery.reading();
}
