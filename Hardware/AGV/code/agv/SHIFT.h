class SHIFT{

  private:

  public:
      // 74hc596
      // ser 11
      // Output Enable 10
      // Register Clock / Latch 8
      // Shift Register Clock 7
      char latchPin =  8 ;
      char clockPin =  7 ;
      char dataPin  = 9 ;
      char enblPin  = 10 ;

      byte val = 0b11111111 ;
    

  SHIFT(){
      // pin setup
      pinMode(latchPin, OUTPUT);
      pinMode(dataPin, OUTPUT);  
      pinMode(clockPin, OUTPUT);
      pinMode(11,INPUT); // pin block
      pinMode(enblPin, OUTPUT);
      digitalWrite(enblPin,LOW);
  }

  void set( byte mask , byte value  ){
      // mask - select the bit range
      // value - new value
      val = ((val)&(~mask)) | value ; // 
      
      updateShiftRegister();
      delay(200);
      val = 255 ;
      updateShiftRegister();
      delay(200);
      
    
  }

  
 
  void updateShiftRegister()
  {
       digitalWrite(clockPin,LOW);
       digitalWrite(latchPin, HIGH);
       shiftOut(dataPin, clockPin, LSBFIRST, val);
       digitalWrite(latchPin, LOW);

  }

  void printing(){
    
  }
  
};
