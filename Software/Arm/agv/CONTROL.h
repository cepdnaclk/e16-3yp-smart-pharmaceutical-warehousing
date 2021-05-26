

class CONTROL{
  private:
     

  public:
 
  
  CONTROL(){
      
      

  }
  void FSM(){

     String k = mqtt_in.substring(0,mqtt_in.length()-2);
     
     //Serial.println(mqtt_in);
     if(k.equals("Test")){
        mqtt_in = "llll";
        motor.rotate();
        Serial.println("ok");
     }
    // line_correction();
        

     
  }

  void state_machine(){
    
  }


  void collision(){
    
  }
  void IR(){
    
  }
  void line_correction(){
      char LEFT_SENSOR =  1 ;
      char RIGHT_SENSOR = 1 ;
      for( char i = 0 ; i < 6 ; i++){
        LEFT_SENSOR += IR_arr[i] ;
        RIGHT_SENSOR+= IR_arr[i+6] ;
      }
     
      Serial.print(LEFT_SENSOR);
      Serial.print('\t');
      Serial.println(RIGHT_SENSOR);
      if(RIGHT_SENSOR < 50 & LEFT_SENSOR < 50) {
        motor.forward( LEFT_SENSOR , RIGHT_SENSOR ); //FORWARD
      }
       else if(RIGHT_SENSOR>50 & LEFT_SENSOR>50) {
        motor.Stop(); //STOP
       }
       
       else if(RIGHT_SENSOR < 50 < LEFT_SENSOR) {
          motor.left(LEFT_SENSOR); //Move Left
       }
       
       else if(RIGHT_SENSOR > 50 > LEFT_SENSOR ) {
        
        motor.right(RIGHT_SENSOR); //Move Right
      }
       

  }


  
}control;
