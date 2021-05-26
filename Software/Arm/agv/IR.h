class IR {

  private:

  public:
  

  char sobel_con = 2 ;
  
  SHIFT shift ;
  
  IR(){
    // A0,1,2,3,6,7
    
    
  }
/*
  void sobel_operator(){
    IR_read();
   // Serial.print("\t");
    
    for(char i = 10 ; i > 0 ; i --){
      sobel[i-1] = abs(IR_arr[i-1]*(-sobel_con)+IR_arr[i+1]*(sobel_con)) ;

    }
  }*/
  
  void IR_read(){
      

      oddIROn();
      evenIROn();
      oddIROff();
      evenIROff();
      
      for(char i = 0 ; i <= 11 ; i++){
       
       // input convert into 1 and zero
        if ( IR_arr[i] < 300 ){
          IR_arr[i] = 0 ;
        }else{
          IR_arr[i] = 1 ;
        }
      }

        IR_arr[0] = 1*IR_arr[0];
        IR_arr[1] = 5*IR_arr[1];
        IR_arr[2] = 50*IR_arr[2];
        IR_arr[3] = 20*IR_arr[3];
        IR_arr[4] = 5*IR_arr[4];
        IR_arr[5] = 1*IR_arr[5];
        IR_arr[6] = 1*IR_arr[6];
        IR_arr[7] = 5*IR_arr[7];
        IR_arr[8] = 20*IR_arr[8];
        IR_arr[9] = 50*IR_arr[9];
        IR_arr[10] = 5*IR_arr[10];
        IR_arr[11] = 1*IR_arr[11];

        
      
      
  }

  void evenIROff(){
    shift.set(0b00001110,0b00001010); // irled and ir rec on 
    delay(1);
    IR_arr[0]  -= analogRead(A7);
    IR_arr[2]  -= analogRead(A6);
    IR_arr[4]  -= analogRead(A3);
    IR_arr[6]  -= analogRead(A2);
    IR_arr[8]  -= analogRead(A1);
    IR_arr[10] -= analogRead(A0); 
    

    shift.set(0b00001110,0b00001110);  // irled and ir rec off
      
  }

  void oddIROff(){
    shift.set(0b00001110,0b00001100); // irled and ir rec on 
    delay(1);
    IR_arr[1]  -= analogRead(A7);
    IR_arr[3]  -= analogRead(A6);
    IR_arr[5]  -= analogRead(A3);
    IR_arr[7]  -= analogRead(A2);
    IR_arr[9]  -= analogRead(A1);
    IR_arr[11] -= analogRead(A0); 


    shift.set(0b00001110,0b00001110);  // irled and ir rec off
  }

  void oddIROn (){
    shift.set(0b00001110,0b00000100); // irled and ir rec on 
    delay(1);
    IR_arr[1]  = analogRead(A7);
    IR_arr[3]  = analogRead(A6);
    IR_arr[5]  = analogRead(A3);
    IR_arr[7]  = analogRead(A2);
    IR_arr[9]  = analogRead(A1);
    IR_arr[11] = analogRead(A0); 


    shift.set(0b00001110,0b00001110);  // irled and ir rec off
    
  }

  void evenIROn(){
    shift.set(0b00001110,0b00000010); // irled and ir rec on 
    delay(1);
    IR_arr[0]  = analogRead(A7);
    IR_arr[2]  = analogRead(A6);
    IR_arr[4]  = analogRead(A3);
    IR_arr[6]  = analogRead(A2);
    IR_arr[8]  = analogRead(A1);
    IR_arr[10] = analogRead(A0); 
    

    shift.set(0b00001110,0b00001110);  // irled and ir rec off
  }
}ir;
