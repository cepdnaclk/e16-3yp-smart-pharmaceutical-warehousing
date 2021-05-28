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
    
    const char* mqtt_topic = "SERVER";
    const char* mqtt_username = "praveen";
    const char* mqtt_password = "Pra350een";
    // The client id identifies the ESP8266 device. Think of it a bit like a hostname (Or just a name, like Greg).
    const char* clientID = "ESP12E";

    // Initialise the WiFi and MQTT Client objects
    
    
    
      
  public:

    //
    Display disp ;
    char qos = 2 ;
 
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
      IP = IpAddress2String(WiFi.localIP());
      disp.play(IP);
     
      client.setServer(mqtt_server, mqttPort);
      
      client.setCallback(callback);
    
    // Connect to MQTT Broker
    // client.connect returns a boolean value to let us know if the connection was successful.
    // If the connection is failing, make sure you are using the correct MQTT Username and Password (Setup Earlier in the Instructable)
    while (!client.connected()) {
      if (client.connect(clientID, mqtt_username, mqtt_password)) {
        disp.play("MQTT cont !");
        pub("IP:"+IpAddress2String(WiFi.localIP()) +" ");
      }
      else {
        disp.play("MQTT failed...");
      }

    }

    client.publish(mqtt_topic, "Hello from ARM1 ");
    client.subscribe("ARM1");
    
  }

  void pub( String mes ) {
    int k = mes.length();
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

  void disPlay(String mes){ // msg publish on display
    disp.play(mes);
  }
  
  
}mqtt;  


void callback(char* topic, byte* payload, unsigned int length) {
   
    //Serial.print("Message arrived in topic: ");
    //Serial.println(topic);
   
    mqtt.disPlay("Message:");
    String message = "";
    for (int i = 0; i < length; i++) {
      //Serial.print((char)payload[i]);
      message += (char)payload[i] ;
    }
    mqtt.disPlay(message);
    // battery life feed back
    if(message.equals("Battery")) {
      mqtt.pub("Battery:" +String(batteryPercentage)+" ");
      disp.play("Battery:" +String(batteryPercentage)+"         ");
    }else if(message.equals("LCD backlight")){
        
        
    }else if(message.equals("SERVER")){
         // wellocome msg
        
        delay(50);
        disp.play("Hello server"); 
        disp.play("IP address:");
        disp.play(IP);
        mqtt.pub("IP:"+IP+" ");
        
        String tem = "Type:ARM " ;
        mqtt.pub(tem);
        tem = "ID:1 ";
        disp.play("ARM ID:1");
        
        mqtt.pub(tem);
  
        delay(2000);
        Serial.println("station");
        
        disp.play("LCD backlight ON            .");
        disp.backlight_ON();
        delay(100);
        disp.play("                              ");
        disp.play("LCD bl off            .");
        disp.backlight_OFF();
        delay(1000);
        disp.play("LCD bl ON            .");
        disp.backlight_ON();
        mqtt.pub("LCD ");

        // motor test

        delay(50);
        disp.play("stepper motor");
        disp.play("testing");
        Serial.print("limit");
        delay(4000);
        mqtt.pub("stepper: calibrate " );
        mqtt.pub("limit stwitch:tested");
        disp.play("Motors: test");
        mqtt.pub("Motors: encoder error ");
        disp.play("encoder error");
        Serial.print("Station");
        delay(4000);
        mqtt.pub("Station:Null");


        delay(1000);
        
        
        
    }
   
}
