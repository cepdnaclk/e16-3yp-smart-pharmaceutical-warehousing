class MOTION{

  private:
    
  public:
    char speed_left = 500 ;
    char speed_right = 500 ;
  MOTION(){
    
  }

  left(){
    //Serial.println("motor");
    pinMode(5,OUTPUT);
    analogWrite(5,speed_left);
    shift.set(0b11000000,0b01000000);
  }

   right(){
    pinMode(6,OUTPUT);
    analogWrite(6,speed_right);
    shift.set(0b00110000,0b00100000);
  }

  
}motor;
