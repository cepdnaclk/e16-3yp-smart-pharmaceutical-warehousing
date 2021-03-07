class IR
{

  private:
   
    String array ;
//Serial.begin(9600);
  public:
   IR(){
    /*
     DDRB |= (0b00001100) ;

     
     */
     digitalWrite(10, HIGH);
     digitalWrite(11, HIGH);
     digitalWrite(12, HIGH);
     pinMode(12, OUTPUT); 
     for ( int i = 0 ; i <= 7 ; i++ ){
       //digitalWrite(A0+i, LOW );
       pinMode(A0+i,INPUT );
     }
   };

   void read(){

    
     array  = "up:1024, down:900, " ;
     //array = "" ;
     int k = 0 ;
     for( int i = 0; i <=  7; i++ ){
        digitalWrite(12, !LOW );
        k = analogRead(A0+i) ;
        delay(5);
        //digitalWrite(12, HIGH); 
        //k = k - analogRead(A0+i) ;
        //if (k < 0 ){
          //k = 0 ;
        //}
        array = array +"my"+(String(i))+":"+ (String(k)) + ", "  ;

     }
     
     
    
    
   }


  void print(){

    Serial.println(array);
  }


};
