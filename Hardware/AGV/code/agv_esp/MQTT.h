void callback(char* topic, byte* payload, unsigned int length);

const char* mqtt_server = "192.168.1.3";
const int mqttPort = 1883;
WiFiClient wifiClient;
PubSubClient client(mqtt_server, mqttPort, wifiClient); // 1883 is the listener port for the Broker

class MQTT{

  private:
    // Make sure to update this for your own WiFi network!
    const char* ssid = "SLT-Fiber";
    const char* wifi_password = "home@12369";
    
    const char* mqtt_topic = "server";
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
        disp.play("Connected to MQTT Broker!");
        
      }
      else {
        Serial.println("Connection to MQTT Broker failed...");
      }

    }

    client.publish("server", "Hello from AGV1 ");
    client.subscribe("agv1");
    
  }

  void pub( String mes ) {
    char k = mes.length();
    char text[k]  ;
    mes.toCharArray(text,k);
    client.publish(mqtt_topic, text,qos);
      

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

  
  
}mqtt;  


void callback(char* topic, byte* payload, unsigned int length) {
   
    Serial.print("Message arrived in topic: ");
    Serial.println(topic);
   
    Serial.print("Message:");
    String message = "";
    for (int i = 0; i < length; i++) {
      Serial.print((char)payload[i]);
      message += (char)payload[i] ;
    }
    
    // battery life feed back
    if(message.equals("battery")) {
      mqtt.pub(String(batteryPercentage)+"");
    }else{
      
    }
   
}
