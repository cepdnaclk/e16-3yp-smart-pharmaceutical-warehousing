class UART{

String incomingByte ; 

  public:
  UART(){
     printline("UART",0);
  }

  void loop(){
    if (Serial.available() > 0) {
      incomingByte = "" ;
    // read the incoming byte:
       incomingByte = Serial.readString();

      printline(String(incomingByte),0); 

  }

  }
  
};
