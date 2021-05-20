class Battery{
  private:
  public:
    Display disp ;
  
  Battery(){
     
  }

  
  void reading(){
    int x = analogRead(A0);
    
    batteryPercentage = (x-775)*100/155;
    // add battery error message
  }
};
