class IR {

  private:

  public:
  int val = 0 ;
  char An0 = A0 ;
  SHIFT shift ;
  
  IR(){
    // A0,1,4,5,6,7
    
    
  }
  void IR_read(){
      val = analogRead(An0);
      Serial.println(val);
  }

  void odd(){
      
    
  }

  void even(){
    
  }
  
};
