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
      /*
      Serial.print(~mask, BIN);
      Serial.print(" & ");
      Serial.print(val, BIN);
      Serial.print(" | ");
      Serial.print(value, BIN);
      Serial.print(" = ");*/
      
      
      val = ((val)&(~mask)) | value ; // 

     // Serial.println(val, BIN);
      //val = value ;
      updateShiftRegister();

      
    
  }

  void test(){
    /*
      set(0b00000000 ,0b00000000);
      delay(1000);
      set(0b00000000 ,0b00001100);
      delay(300);*/

      
  }
 
  void updateShiftRegister()
  {
       //digitalWrite(clockPin,LOW);
       digitalWrite(latchPin, LOW);
       shiftOut(dataPin, clockPin, LSBFIRST, val);
       digitalWrite(latchPin, HIGH);

  }

  void printing(){
    
  }
  
}shift;
