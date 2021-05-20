class CONTROL{
  private:
  public:

  CONTROL(){

  }
  void FSM(){

    String k ;
    k = mqtt_in.substring(0,mqtt_in.length() -2);
    //Serial.println(k.length());
    //Serial.println(k);
    if(k.equals("forward")){
        //Serial.println("go go");
        motor.left();
        motor.right();

        line_correction();
        
    }
    
  }

  void state_machine(){
    
  }


  void collision(){
    
  }
  void IR(){
    
  }
  void line_correction(){
    int left = 0 ; 
    int right = 0 ;
    for( char k = 0 ; k < 6 ; k ++){
      left += ir.IR[k] ;
      right +=ir.IR[k+5] ;
    }
    /*
    Serial.print(left);
    Serial.print('\t');
    Serial.println(right);*/

    if((right != 0 ) & (left != 0) ){
        if ( right > left){
            motor.speed_left = 500*right/left;
            motor.speed_right = 500*left/right ;
            
        }
    }else{
      motor.speed_left = 0 ;
      motor.speed_right = 0 ;
    }
    
  }
  
  
}control;
