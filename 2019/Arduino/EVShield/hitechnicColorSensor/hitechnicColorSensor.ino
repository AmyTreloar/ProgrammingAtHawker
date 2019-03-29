#include <Wire.h>
#include <EVShield.h>
#include <EVs_NXTTouch.h>
#include <EVs_HTColorSensor.h>

EVShield evshield(0x34, 0x36);
EVs_NXTTouch touch;
EVs_HTColorSensor colorSensor1(SH_Bank_A);
EVs_HTColorSensor colorSensor2(SH_Bank_B);

void setup() {
  Serial.begin(9600);
  Serial.println("---------------");
  Serial.println("Initialising HiTechnic Color Sensor test");
  evshield.init(SH_HardwareI2C);
  colorSensor1.init(&evshield, SH_BAS2);
  touch.init(&evshield, SH_BAS1);
  colorSensor2.init(&evshield, SH_BBS2);
  Serial.println("Press Go button to continue");
  //evshield.waitForButtonPress(BTN_GO);

}

void loop() {
  Serial.print(colorSensor1.getColorId()); Serial.print(" "); Serial.print(colorSensor2.getColorId());
  Serial.print(" "); Serial.println(touch.isPressed());
  delay(100);

}
