#include <Wire.h>
#include <EVShield.h>
#include <EVs_HTColorSensor.h>

EVShield evshield(0x34, 0x36);
EVs_HTColorSensor colorSensor(0x02);

void setup() {
  Serial.begin(9600);
  Serial.println("---------------");
  Serial.println("Initialising HiTechnic Color Sensor test");
  evshield.init(SH_HardwareI2C);
  colorSensor.init(&evshield, SH_BAS1);
  Serial.println("Press Go button to continue");
  evshield.waitForButtonPress(BTN_GO);

}

void loop() {
  Serial.println(colorSensor.getColorId());
  delay(100);

}
