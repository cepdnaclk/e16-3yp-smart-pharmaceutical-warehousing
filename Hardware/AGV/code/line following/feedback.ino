void ledBlink(void)
{
   for (int i = 0; i<4; i++)
   { 
      digitalWrite (ledPin, HIGH);
      delay (500);
      digitalWrite (ledPin, LOW);
      delay (500);
   } 
}

//-----------------------------------------------------------------------------

 void checkBTcmd()  
 { 
   while (BT1.available())   //Check if there is an available byte to read
   {
     delay(10); //Delay added to make thing stable 
     char c = BT1.read(); //Conduct a serial read
     device += c; //build the string.
   }  
   if (device.length() > 0) 
   {
     Serial.print("Command received from BT ==> ");
     Serial.println(device); 
     command = device;
     device ="";  //Reset the variable
     BT1.flush();
    } 
}

//------------------------------------------------------------------------
void manualCmd()
{
  switch (command[0])
  {
    case 'f': 
      motorStop(); //turn off both motors
      break;

    case 'w':  
      motorForward();  
      break;

    case 'd':     
      motorTurn(RIGHT, 300);
      motorStop();
      
      break;

   case 'a': 
      motorTurn(LEFT, 300);
      motorStop();
      break;
    
    case 's':  
      motorBackward();
      break;
      
  }
}

//------------------------------------------------------------------------
void sendBTdata (int data) // send data to BT

{
    digitalWrite (ledPin, HIGH);
    BT1.print("Data from Arduino");
    BT1.print(data);
    BT1.print(" xx");
    BT1.println('\n');
    digitalWrite (ledPin, LOW);
}

//--------------------------------------------------------
void calculatePID()
{
  P = error;
  I = I + error;
  D = error-previousError;
  PIDvalue = (Kp*P) + (Ki*I) + (Kd*D);
  previousError = error;
}

//-----------------------------------------------
void testLineFollowSensors()
{
     int LFS0 = digitalRead(lineFollowSensor0);
     int LFS1 = digitalRead(lineFollowSensor1);
     int LFS2 = digitalRead(lineFollowSensor2);
     int LFS3 = digitalRead(lineFollowSensor3);
     int LFS4 = digitalRead(lineFollowSensor4);
     
     Serial.print ("LFS: L  0 1 2 3 4  R ==> "); 
     Serial.print (LFS0); 
     Serial.print (" ");
     Serial.print (LFS1); 
     Serial.print (" ");
     Serial.print (LFS2); 
     Serial.print (" ");
     Serial.print (LFS3); 
     Serial.print (" ");
     Serial.print (LFS4); 
     Serial.print ("  ==> ");
    
     Serial.print (" P: ");
     Serial.print (P);
     Serial.print (" I: ");
     Serial.print (I);
     Serial.print (" D: ");
     Serial.print (D);
     Serial.print (" PID: ");
     Serial.println (PIDvalue);
}
