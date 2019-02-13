#include <EVShield.h>
#include <EVs_EV3Touch.h>


EVShield evshield(0x34, 0x36);
EVs_EV3Touch touch1;

bool touching; 
void setup() {
  Serial.begin(9600);
  Serial.println("--------------------------------");
  Serial.println("Initialising Touch/Button");

  evshield.init(SH_HardwareI2C);
  touch1.init(&evshield, SH_BAS1);
  Serial.println("Press go button to continue");
  evshield.waitForButtonPress(BTN_GO);

}

void loop() {
  touching = touch1.isPressed();
  Serial.println(touching);
  if (touching){
    evshield.bank_a.ledSetRGB(255,0,0);
    evshield.bank_b.ledSetRGB(0,0,255);
  } else {
    evshield.bank_a.ledSetRGB(0,0,0);
    evshield.bank_b.ledSetRGB(0,0,0);
  }
  delay(100);

}
