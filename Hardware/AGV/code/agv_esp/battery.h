class Battery{
  private:
  public:
    Display disp ;
  
  Battery(){
     
  }

  
  void reading(){
    int x = analogRead(A0);
    Serial.println(x);
  }
};
