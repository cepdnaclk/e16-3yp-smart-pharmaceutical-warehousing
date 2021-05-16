void callback(char* topic, byte* payload, unsigned int length) {
   
    Serial.print("Message arrived in topic: ");
    Serial.println(topic);
   
    Serial.print("Message:");
    for (int i = 0; i < length; i++) {
      Serial.print((char)payload[i]);
    }
   
    Serial.println();
    Serial.println("-----------------------");
   
}


const char* mqtt_server = "192.168.1.3";
const int mqttPort = 1883;
WiFiClient wifiClient;
PubSubClient client(mqtt_server, mqttPort, wifiClient); // 1883 is the listener port for the Broker

class MQTT{

  private:
    // Make sure to update this for your own WiFi network!
    const char* ssid = "SLT-Fiber";
    const char* wifi_password = "home@12369";
    
    const char* mqtt_topic = "my_agv_test";
    const char* mqtt_username = "praveen";
    const char* mqtt_password = "Pra350een";
    // The client id identifies the ESP8266 device. Think of it a bit like a hostname (Or just a name, like Greg).
    const char* clientID = "ESP12E";

    // Initialise the WiFi and MQTT Client objects
    
    
    
      
  public:

    //
    Display disp ;
    char qos = 0 ;
 
  MQTT(){

      disp.play("Connecting to ");
      disp.play(ssid);
    
  }


  void connection(){
      
    
      // Connect to the WiFi
      WiFi.begin(ssid, wifi_password);
      
      // Wait until the connection has been confirmed before continuing
      while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        disp.play("...");
      }

        // Debugging - Output the IP Address of the ESP8266
      disp.play("WiFi connected");
      disp.play("IP address: ");
      
      disp.play(IpAddress2String(WiFi.localIP()));
    
      client.setServer(mqtt_server, mqttPort);
      client.setCallback(callback);
    
    // Connect to MQTT Broker
    // client.connect returns a boolean value to let us know if the connection was successful.
    // If the connection is failing, make sure you are using the correct MQTT Username and Password (Setup Earlier in the Instructable)
    while (!client.connected()) {
      if (client.connect(clientID, mqtt_username, mqtt_password)) {
        Serial.println("Connected to MQTT Broker!");
        
      }
      else {
        Serial.println("Connection to MQTT Broker failed...");
      }

    }

    client.publish("agv/test", "Hello from ESP8266");
    client.subscribe("server/my");
    
  }

  void pub() {
    int k = 0 ; 
    char text[50] ;
    String mes =  "Button pressed !" ;
    //while(1){
      mes = "Button pressed" ;
      mes += String(k) ;
      mes += "ll" ;
      mes.toCharArray(text,50);
      client.publish(mqtt_topic, text,qos);
      
      k++;
    //}
    
  }
  
  void loop(){
    
    client.loop();

    
  }
  
  String IpAddress2String(const IPAddress& ipAddress)
  {
    return String(ipAddress[0]) + String(".") +\
    String(ipAddress[1]) + String(".") +\
    String(ipAddress[2]) + String(".") +\
    String(ipAddress[3])  ; 
  }

  
  
};  
