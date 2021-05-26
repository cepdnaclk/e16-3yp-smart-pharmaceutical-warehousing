class Battery{
  private:
  public:
    Display disp ;
  
  Battery(){
     
  }

  
  void reading(){
    int x = analogRead(A0);
    x = (x-775)*100/155 ; 
    if( (10 < x) & (x < 100) ){
      batteryPercentage = String(x)+"%";
    }else if( (0<x)&(x<10) ){
      batteryPercentage = "battery low" ; 
    }else {
      batteryPercentage = "battery error" ; 
    }
    // add battery error message
  }
};
