#include <Wire.h>
#include <EVShield.h>
#include <EVs_NXTTouch.h>
#include <EVs_HTColorSensor.h>

EVShield evshield(0x34, 0x36);
EVs_NXTTouch touch;
EVs_HTColorSensor colorSensor1;
EVs_HTColorSensor colorSensor2;

void setup() {
  Serial.begin(9600);
  Serial.println("---------------");
  Serial.println("Initialising HiTechnic Color Sensor test");
  evshield.init(SH_HardwareI2C);
  colorSensor1.init(&evshield, SH_BAS2);
  touch.init(&evshield, SH_BAS1);
  colorSensor2.init(&evshield, SH_BBS2);

  Serial.print(colorSensor1.checkAddress());
  Serial.print(" ");
  Serial.print(colorSensor2.checkAddress());
  Serial.print(" ");
  Serial.print(colorSensor1.getAddress());
  Serial.print(" ");
  Serial.print(colorSensor2.getAddress());
  colorSensor2.setAddress(0x3);
  Serial.print(" ");
  Serial.println(colorSensor2.getAddress());
  Serial.println("Press Go button to continue");
  evshield.waitForButtonPress(BTN_GO);
}

void loop() {
  Serial.print(colorSensor1.getColorId()); Serial.print(" "); 
  Serial.print(colorSensor2.getColorId());
  Serial.print(" "); Serial.println(touch.isPressed());
  delay(1000);

}
