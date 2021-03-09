

LiquidCrystal_I2C lcd(0x27, 20, 2);

void lcd_setup(){
    lcd.init();                      // initialize the lcd 
    lcd.init();
    // Print a message to the LCD.
    lcd.backlight();
    lcd.setCursor(1, 0 );
    //lcd.print( "kknjkv" );
}

void lcdprint(char k , String test){
  lcd.setCursor(1, k );
  lcd.print(test); // Start Printing
}

void lcdclean(){
  lcd.clear();
}
