

//
// Detect colors using TCS230.
//

// Arduino uno pins for control of TCS230
#define TCS320_OE 7
#define TCS320_S0 10
#define TCS320_S1 11
#define TCS320_S2 2
#define TCS320_S3 3
#define TCS320_OUT 4

#define variance 50  // Acceptable detection error 2%.

#define SEL_RED  \
   digitalWrite(TCS320_S2,LOW);digitalWrite(TCS320_S3,LOW)
#define SEL_GREEN \
   digitalWrite(TCS320_S2,HIGH);digitalWrite(TCS320_S3,HIGH)
#define SEL_BLUE \
   digitalWrite(TCS320_S2,LOW);digitalWrite(TCS320_S3,HIGH)
#define SEL_CLEAR \
   digitalWrite(TCS320_S2,HIGH);digitalWrite(TCS320_S3,LOW)

#define TWO_PER \
   digitalWrite(TCS320_S0,LOW);digitalWrite(TCS320_S1,HIGH);

#define debug(a) Serial.println((a));


#define NUMCOL 5

// int RGB[NUMCOL][3]; // Five colors with 3 elements.
// Array of NUMCOL strings len 10. 11 for null.
// char colname[NUMCOL][11];

// Typical values for 2% dividers (set variance to 50).
int RGB[NUMCOL][3]={
   {248,647,393},
   {188,261,265},
   {404,710,546},
   {506,493,304},
   {930,1199,837},
};

char colname[NUMCOL][11]={
"red",
"yellow",
"brown",
"blue",
"black",
};

////////////////////////////////////////////////////////////////
void setup() {

   pinMode(TCS320_OE,OUTPUT);
   pinMode(TCS320_S0,OUTPUT);
   pinMode(TCS320_S1,OUTPUT);
   pinMode(TCS320_S2,OUTPUT);
   pinMode(TCS320_S3,OUTPUT);
   pinMode(TCS320_OUT,INPUT);

   TWO_PER;

   digitalWrite(TCS320_OE,LOW); // On always.

   Serial.begin(115200);
   Serial.println("TCS230 color detector");
}

////////////////////////////////////////////////////////////////
unsigned long get_TCS230_reading(void) {
  unsigned long val;
  noInterrupts();
  val = pulseIn(TCS320_OUT,HIGH,20000); // 2000us=2ms  2Hz min.
  interrupts();
  return val;
}

static int clr,red,green,blue;

////////////////////////////////////////////////////////////////
uint16_t detect(void) {
   unsigned long val;

    SEL_RED;
    red = val = get_TCS230_reading();
    Serial.print("RED: "); Serial.print(val);

    SEL_GREEN;
    green = val = get_TCS230_reading();
    Serial.print(" GREEN: "); Serial.print(val);

    SEL_BLUE;
    blue = val = get_TCS230_reading();
    Serial.print(" BLUE: "); Serial.print(val);

    Serial.print(" \n");
}

////////////////////////////////////////////////////////////////
int withinEQ(int c, int xl, int xh) {
   if (c>=xl && c<=xh) return 1;
   return 0;
}

////////////////////////////////////////////////////////////////
// Compare a value to a value and variance.
int compare(int c, int v, int err) {
int xh=v+err, xl=v-err;
   if (withinEQ(c,xl,xh)) return 1;
   return 0;
}

////////////////////////////////////////////////////////////////
void loop() {
uint8_t chr,i,fnd;

   if (Serial.available()>0) {

      chr = Serial.read(); // Consume.

      // Find color match.
      detect();
      fnd=0;
      for (i=0;i<NUMCOL;i++) {
         if ( compare(red,RGB[i][0],variance) &&
              compare(green,RGB[i][1],variance) &&
              compare(blue,RGB[i][2],variance)
            ) { // Found
              Serial.print("Col is :");
              Serial.println(colname[i]);
              fnd=1;
              break;
            }
      }
      if (!fnd) Serial.println("NOT Found");
   }
}
