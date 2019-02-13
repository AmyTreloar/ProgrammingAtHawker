#include <EVShield.h>
#include <EVs_NXTLight.h>

EVShield evshield(0x34, 0x36);
EVs_NXTLight lightSensor;

int lightValue;
void setup() {
  Serial.begin(9600);
  Serial.println("----------------");
  Serial.println("Starting NXT Light sensor");
  evshield.init(SH_HardwareI2C);
  lightSensor.init(&evshield, SH_BAS1);
  lightSensor.setReflected();
  //lightSensor.setAmbient();
  Serial.println("Press Go button to Continue");
  evshield.waitForButtonPress(BTN_GO);
}

void loop() {
  lightValue = lightSensor.readRaw();
  Serial.print("Light level: "); Serial.println(lightValue);
  delay(100);
}
