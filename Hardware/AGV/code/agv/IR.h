class IR {

  private:

  public:
  int IR[12]  ;
  int sobel[10];
  char sobel_con = 2 ;
  char An0 = A0 ;
  SHIFT shift ;
  
  IR(){
    // A0,1,2,3,6,7
    
    
  }

  void sobel_operator(){
    IR_read();
   // Serial.print("\t");
    
    for(char i = 10 ; i > 0 ; i --){
      sobel[i-1] = abs(IR[i-1]*(-sobel_con)+IR[i+1]*(sobel_con)) ;
      /*
      if (sobel[i-1] > 600 ){
        Serial.print("*");
      }else if( sobel[i-1] < 400 ){
        Serial.print("-");
      }
      //Serial.print(sobel[i-1] );
      Serial.print("\t");
    }
    Serial.println();*/
    }
  }
  
  void IR_read(){
      

      oddIROn();
      evenIROn();
      oddIROff();
      evenIROff();
      
      for(char i = 11 ; i >= 0 ; i--){
      // Serial.print(IR[i]);
       
        if ( IR[i] < 250 ){
          Serial.print("*");
        }else if( IR[i] > 450 ){
          Serial.print("-");
        }
        Serial.print('\t');
      }
      Serial.println();
  }

  void oddIROff(){
    shift.set(0b00001110,0b00001010); // irled and ir rec on 
    delay(5);
    IR[1]  -= analogRead(A0);
    IR[3]  -= analogRead(A1);
    IR[5]  -= analogRead(A2);
    IR[7]  -= analogRead(A3);
    IR[9]  -= analogRead(A6);
    IR[11] -= analogRead(A7); 
    

    shift.set(0b00001110,0b00001110);  // irled and ir rec off
      
  }

  void evenIROff(){
    shift.set(0b00001110,0b00001100); // irled and ir rec on 
    delay(5);
    IR[0]  -= analogRead(A0);
    IR[2]  -= analogRead(A1);
    IR[4]  -= analogRead(A2);
    IR[6]  -= analogRead(A3);
    IR[8]  -= analogRead(A6);
    IR[10] -= analogRead(A7); 


    shift.set(0b00001110,0b00001110);  // irled and ir rec off
  }

  void evenIROn (){
    shift.set(0b00001110,0b00000100); // irled and ir rec on 
    delay(1);
    IR[0]  = analogRead(A0);
    IR[2]  = analogRead(A1);
    IR[4]  = analogRead(A2);
    IR[6]  = analogRead(A3);
    IR[8]  = analogRead(A6);
    IR[10] = analogRead(A7); 


    shift.set(0b00001110,0b00001110);  // irled and ir rec off
    
  }

  void oddIROn(){
    shift.set(0b00001110,0b00000010); // irled and ir rec on 
    delay(1);
    IR[1]  = analogRead(A0);
    IR[3]  = analogRead(A1);
    IR[5]  = analogRead(A2);
    IR[7]  = analogRead(A3);
    IR[9]  = analogRead(A6);
    IR[11] = analogRead(A7); 
    

    shift.set(0b00001110,0b00001110);  // irled and ir rec off
  }
}ir;
