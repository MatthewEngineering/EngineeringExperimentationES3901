#include "HX711.h" //This library can be obtained here http://librarymanager/All#Avia_HX711

#define LOADCELL_DOUT_PIN  3
#define LOADCELL_SCK_PIN  2
unsigned long StartTime = 0;
HX711 scale;

void setup() {
  Serial.begin(9600);

  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  scale.tare();    //Assuming there is no weight on the scale at start up, reset the scale to 0
//  start a timer
  StartTime = millis();
  
}

float calibrate(float info){
  return ((info * 100) / -109000);
}


void loop() {
  float weight = scale.get_units();
  weight = calibrate(weight);
  unsigned long CurrentTime = millis();
  float ElapsedTime = (CurrentTime-StartTime)/1000.0;
  Serial.print(weight, 2); //scale.get_units() returns a float
  Serial.print(", \t"); 
  Serial.print(ElapsedTime, 3); //scale.get_units() returns a float
  Serial.println();
}
