#include <Wire.h>
//  by John Sullivan and Ahmet Can Sabuncu, ME3902 Summer 2021
//
#include <Adafruit_ADS1X15.h>  // same library for both the ads1015 and ads1115
Adafruit_ADS1115 ads1115;  // Declare an instance of the ADS1115 at address slot 0x48
int16_t rawADCvalue;  // The is where we store the value we receive from the ADS1115
                      //  int16_t is a 16 bit signed integer range = -32768 to +32767
                      // scalefactor = max Voltage /(  (2^15)-1 = max Voltage/(32767) for 16 bit with most
                      //   significant bit reserved for sign (+ or -)

float volts = 0.0;        // The result of applying the scale factor to the raw value

float bit_res = 0.1875000;
//float bit_res = 0.1250000;
//float bit_res = 0.0625000;
//float bit_res = 0.0312500;
//float bit_res = 0.0156250;
//float bit_res = 0.0078125;    //  This is the bit resolution in [mV] will change with the gain, please refer to the table below

float uV = 0.0;           //  This is just volts times a million [uV]
float a0 = 0, a1 = 2.5928e-2, a2 = -7.602961e-7, a3 = 4.637791e-11;  //  These are the NIST coefficients for converting voltage readings to temperature
float a4 = -2.165394e-15, a5 = 6.048144e-20, a6 = -7.293422e-25;    //  These are the NIST coefficients for converting voltage readings to temperature

// PLEASE LOOK UP THE NIST COEFFICIENTS FOR YOUR THERMOCOUPLE


float TempDegC=0;
unsigned long StartTime = 0;
//                                 //  Gain      Max Volt     ads1015          ads1115
// ads1115.setGain(GAIN_TWOTHIRDS);// 2/3x gain +/- 6.144V  1 bit = 3mV (default)  1 bit = 187.5 micro-V
// ads1015.setGain(GAIN_ONE);      // 1x gain   +/- 4.096V  1 bit = 2mV         1 bit = 125. micro-V
// ads1015.setGain(GAIN_TWO);      // 2x gain   +/- 2.048V  1 bit = 1mV         1 bit =  62.5 micro-V
// ads1015.setGain(GAIN_FOUR);     // 4x gain   +/- 1.024V  1 bit = 0.5mV       1 bit =  31.25 micro-V
// ads1015.setGain(GAIN_EIGHT);    // 8x gain   +/- 0.512V  1 bit = 0.25mV      1 bit =  15.625 micro-V
// ads1015.setGain(GAIN_SIXTEEN);  // 16x gain  +/- 0.256V  1 bit = 0.125mV     1 bit =  7.8125 micro-V

void setup(void)
{
  Serial.begin(9600); 
  ads1115.setGain(GAIN_TWOTHIRDS);  // Set gain to 16x
  ads1115.begin(0x48);
  //  start a timer
  StartTime = millis();
}

float do_calculations(float uV){

//  V = I * R
//  current stays same in series

//  voltage and current in resistor
  float Vr = uV / 1000000;
  float I = Vr / 10000; // 10,000 Ohm Resistor

//  find voltage in thermistor
  float Vt = 5.0 - Vr;
  float Rt = Vt / I;

//  using the Steinhard Hart Equation from Canvas: 
//  setting for this thermistor for this equation
  float Beta = 3950; 
  float To = 22.75+273; // kelvin
  float Ro = 10530;

//  Equation (cut up into intermediates)
  float a_log = log( Rt / Ro);
  float bottom = ( a_log / Beta ) + (1/To);
  float T = 1/bottom;

//  return Rt; // for calibration of Ro
  return T - 273;
}

float perform_calibration(float T){
  return (1.01*T) + 0.234; 
}

void loop(void)
{  
  rawADCvalue = ads1115.readADC_Differential_0_1(); // Differential voltage measurement between A0 and A1 on the ADC chip
  volts = rawADCvalue * bit_res; // Convert rawADC number to voltage in [mV]
  uV = volts*1e3; // Express the voltage in microVolts
//  TempDegC = a0 + a1*uV + a2*pow(uV,2) + a3*pow(uV,3) + a4*pow(uV,4) + a5*pow(uV,5) + a6*pow(uV,6);
  unsigned long CurrentTime = millis();
  float ElapsedTime = (CurrentTime-StartTime)/1000.0;
//  Serial.print("Time (sec) "); 
  Serial.print(ElapsedTime,3); 
//  Serial.print(",   microVolts Measured = ");
//  Serial.print(uV,2);

  float T = do_calculations(uV);

  T = perform_calibration(T);

  Serial.print(",");
//  Serial.print(",   Temperature (deg C) = ");
  Serial.println(T,2);
//  Serial.println();
  delay(500);
}
