void Battery_read();

Scheduler batterycheck;

Task tbattery(60000, TASK_FOREVER, &Battery_read);

char battery_life = 0 ;

class Battery{

  public :
  Battery(){
    pinMode(A0,INPUT);
    batterycheck.init();
    batterycheck.addTask(tbattery);
    tbattery.enable();
  }

  void loop(){
    batterycheck.execute();
  }
  
};

void Battery_read(){
  battery_life =  (analogRead(A0)-188)*100/44;

  if ( battery_life > 100 ){
    battery_life = 100 ;
  }else if( battery_life < 20 ){
    printline( "battery low" ,0) ;
  }
  printline( "Bat:"+String(int(battery_life))+"%  " ,0);
}
