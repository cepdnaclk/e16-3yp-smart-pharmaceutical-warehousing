
#include <ESP8266WiFi.h> // Enables the ESP8266 to connect to the local network (via WiFi)
#include <PubSubClient.h> // Allows us to connect to, and publish to the MQTT broker


#include "display.h"
#include "battery.h"
#include "UART.h"
#include "MQTT.h"

Display  disp;
Battery battery;
UART uart ;
MQTT mqtt ;


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
  mqtt.loop();
  

  
}
