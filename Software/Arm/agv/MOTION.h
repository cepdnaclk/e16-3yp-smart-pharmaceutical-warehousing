
class MOTION{

  private:
    
  public:
     char M1_Speed = 120; // speed of motor 1 

     char RightRotationSpeed = 0; // Right Rotation Speed

     // in1  1000
     // in2  0100
     // in3  0001
     // in4  0010

     // D5 left
     // D6 right
 

  MOTION(){
    
    pinMode(5,OUTPUT);
    pinMode(6,OUTPUT);

  }
  void rotate(){
     shift.set(0b11110000,0b01010000);
     analogWrite(5,M1_Speed);
     analogWrite(6,M1_Speed);
     delay(1000);
     shift.set(0b11110000,0b00000000);

     shift.set(0b11110000,0b10100000);
     analogWrite(5,M1_Speed);
     analogWrite(6,M1_Speed);
     delay(1000);
     shift.set(0b11110000,0b00000000);
  }

  void forward(char left , char right )
  {
     Serial.println("forward");
     analogWrite(5,M1_Speed);
     analogWrite(6,M1_Speed);
     Serial.print(90+ M1_Speed / left );
     Serial.print('\t');
     Serial.println(90+ M1_Speed / right ); 
     analogWrite(5, 90+ M1_Speed / left );
     analogWrite(6, 90+ M1_Speed / right );
     shift.set(0b11110000,0b01100000);
  }

  void right(char x){
    Serial.println("RIGHT");

    
    analogWrite(5,RightRotationSpeed);
    analogWrite(6,M1_Speed);
    shift.set(0b11110000,0b01100000);
  }

  void  left(char x){

    Serial.println("LEFT");
    analogWrite(5,M1_Speed);
    analogWrite(6,RightRotationSpeed);
    shift.set(0b11110000,0b01100000);
  }

    void Stop()
  {
      Serial.println("Stop");
       shift.set(0b11110000,0b00000000);
  }

  void motor_left(){
    
  }
  void motor_right(){
    
  }



}motor; 
