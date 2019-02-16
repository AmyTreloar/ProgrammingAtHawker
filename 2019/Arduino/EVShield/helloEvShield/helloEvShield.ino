#include <EVShield.h>

EVShield evshield(0x34, 0x36);


void setup() {
  Serial.begin(9600);
  Serial.println("--------------------------------");
  Serial.println("Initialising EVShield");

  evshield.init(SH_HardwareI2C);
  Serial.println("Press go button to continue");
  evshield.waitForButtonPress(BTN_GO);

}

void loop() {
  Serial.println("Hello world");
  delay(100);

}
