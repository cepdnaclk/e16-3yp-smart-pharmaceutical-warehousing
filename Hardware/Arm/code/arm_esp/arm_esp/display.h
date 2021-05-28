
#include <LiquidCrystal_I2C.h>

#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

class Display{
 
  

  private:
  public:
    char lower = 0 ;
  
  Display(){
   
      lcd.init();                      // initialize the lcd 
      lcd.init();
    
      // Print a message to the LCD.
      lcd.backlight();
      lcd.setCursor(1,0);
      lcd.print("hello everyone");
      lcd.setCursor(1,1);
      lcd.print("wellcome");
    
  }

  void play(String msg){
     
      if(lower == 1 ){
        lower = 0 ;
        lcd.init();                      // initialize the lcd 
        lcd.init();
     
      }else{
        lower = 1 ;
      }

      // Print a message to the LCD.
      lcd.backlight();
      lcd.setCursor(1,lower);
      lcd.print(msg);


  }

  void backlight_ON(){
    lcd.setBacklight(HIGH);
  }
  void backlight_OFF(){
    lcd.setBacklight(LOW);
  }
  
};
