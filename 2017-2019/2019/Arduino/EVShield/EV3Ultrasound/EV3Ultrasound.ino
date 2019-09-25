#include <EVShield.h>
#include <EVs_EV3Ultrasonic.h>

EVShield evshield(0x34, 0x36);
EVs_EV3Ultrasonic distanceSensor;
float distance;
void setup() {
  Serial.begin(9600);
  Serial.println("----------------------------------------");
  Serial.println("Starting ev3 distance sensor");
  Serial.println("----------------------------------------");

  evshield.init(SH_HardwareI2C);
  distanceSensor.init(&evshield, SH_BAS1);
  Serial.println("Press go button to continue");
  evshield.waitForButtonPress(BTN_GO);
}

void loop() {
  distance = distanceSensor.getDist();
  Serial.println(distance);
  delayMicroseconds(100);
}
