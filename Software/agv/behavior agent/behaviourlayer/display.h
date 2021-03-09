

LiquidCrystal_I2C lcd(0x27,20,4);  // set the LCD address to 0x27 for a 16 chars and 2 line display

void LCD(){
  lcd.init();                      // initialize the lcd 
  lcd.init();
  // Print a message to the LCD.
  lcd.backlight();

}

void printline( String text , int line ){
  lcd.setCursor(0, line );
  lcd.print( text );
}
