
class UART{
  private:

  public:

  UART(){
    
    Serial.begin(115200);
  }

  void RX(){
    
  }

  void TX(){
    Serial.println("hello");
    delay(2000);
  }
  
};
