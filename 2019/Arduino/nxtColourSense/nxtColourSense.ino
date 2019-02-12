#include <EVShield.h>
#include <EVs_NXTColor.h>

EVShield evshield(0x34, 0x36);
EVs_NXTColor colorSensor;

enum color_value {
  CLR_NONE = 0, 
  CLR_BLACK = 1, 
  CLR_BLUE = 2, 
  CLR_GREEN = 3, 
  CLR_YELLOW = 4, 
  CLR_RED = 5, 
  CLR_WHITE = 6,
  CLR_BROWN = 7,
};
int clr_value;
String getColourValue(int clr){
  switch(clr){
    case CLR_NONE: return "No Colour";
    case CLR_BLACK: return "Black";
    case CLR_GREEN: return "Green";
    case CLR_YELLOW: return "Yellow";
    case CLR_RED: return "Red";
    case CLR_WHITE: return "White";
    case CLR_BROWN: return "Brown";
    default: return "Error";
  }
}

void setup() {
  Serial.begin(9600);
  Serial.println("-------------------");
  Serial.println("Initialising NXT Colour Sensor Test");

  evshield.init(SH_HardwareI2C);
  colorSensor.init(&evshield, SH_BAS1);
  colorSensor.setType(SH_Type_COLORFULL);
  Serial.println("Press Go button to continue");
  evshield.waitForButtonPress(BTN_GO);

}

void loop() {
  clr_value = colorSensor.readColor();
  Serial.print("Colour: "); Serial.print(getColourValue(clr_value));
  Serial.print(" "); Serial.println(clr_value);
  delay(100);

}
