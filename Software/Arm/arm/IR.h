class IR{

  private:
    char prox = A0 ;
    char IR   = A2 ;
  public:
  int analog ;

  // prox A0 
  // IR led on/off A2
  IR(){
    
    pinMode(IR,OUTPUT);
    digitalWrite(IR,LOW);
  
  }

  void read(){
    // ir filtering
    
    int tem =  analogRead(prox);
    digitalWrite(IR,HIGH);
    delay(2);
    analog = analogRead(prox) -tem  ;
    digitalWrite(IR,LOW);
    Serial.println(analog);
    delay(100);
    
  }
  
  
};
