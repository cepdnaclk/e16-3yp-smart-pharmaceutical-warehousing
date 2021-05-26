
class UART{
  private:
    String incomingByte = "";
  public:

  UART(){
    
    Serial.begin(115200);
  }

  void RX(){
    if (Serial.available() > 0) {
      // read the incoming byte:
      mqtt_in = "" ;
      mqtt_in = Serial.readStringUntil('\0');
      
      // say what you got:
      
      //Serial.println(mqtt_in);
      
    }
  }

  void TX(){
    Serial.println("hello");
    delay(2000);
  }
  
};
