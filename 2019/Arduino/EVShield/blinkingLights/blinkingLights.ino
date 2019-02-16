#include <EVShield.h>

EVShield evshield(0x34, 0x36);

int counter = 0;
void setup() {
  Serial.begin(9600);
  Serial.println("--------------------------------");
  Serial.println("Initialising EVshield on board LEDs");

  evshield.init(SH_HardwareI2C);
  evshield.bank_a.ledSetRGB(0, 255, 0);
  evshield.bank_b.ledSetRGB(0, 255, 0);

  
  Serial.println("Press go button to continue");
  evshield.waitForButtonPress(BTN_GO);

}

void loop() {
  counter++; 
  if (counter % 2 == 0){
    evshield.bank_a.ledSetRGB(255, 0, 0);
    evshield.bank_b.ledSetRGB(0, 0, 255);
    Serial.println("LEFT: Red RIGHT: Blue");
  } else {
    evshield.bank_a.ledSetRGB(0, 0, 255);
    evshield.bank_b.ledSetRGB(255, 0, 0);
    Serial.println("LEFT: blue RIGHT: Red");
  }
  delay(500);

}
