#include <EVShield.h>
#include <EVs_EV3Color.h>

EVShield evshield(0x34, 0x36);
EVs_EV3Color leftLightSensor;
EVs_EV3Color rightLightSensor;

int leftReading;
int rightReading;
void setup() {
  Serial.begin(9600);
  Serial.println("----------------------------------------");
  Serial.println("Starting ev3 line sensor using colour sensors");
  Serial.println("----------------------------------------");

  evshield.init(SH_HardwareI2C);
  leftLightSensor.init(&evshield, SH_BAS1);
  leftLightSensor.setMode(MODE_Color_ReflectedLight); 
  rightLightSensor.init(&evshield, SH_BBS1);
  rightLightSensor.setMode(MODE_Color_ReflectedLight);
  Serial.println("Press go button to continue");
  evshield.waitForButtonPress(BTN_GO);
}

void loop() {
  leftReading = leftLightSensor.getVal();
  rightReading = rightLightSensor.getVal();
  Serial.print(leftReading); Serial.print(" "); Serial.println(rightReading);
}
