#include <EVShield.h>
#include <EVs_NXTTouch.h>
#include <Wire.h>


EVShield evshield(0x34, 0x36);
EVs_NXTTouch touch1;

bool touching; 
void setup() {
  Serial.begin(9600);
  Serial.println("--------------------------------");
  Serial.println("Initialising Touch/Button motor");

  evshield.init(SH_HardwareI2C);
  touch1.init(&evshield, SH_BAS1);
  evshield.bank_a.motorReset();
  evshield.bank_b.motorReset();
  Serial.println("Press go button to continue");
  evshield.waitForButtonPress(BTN_GO);

}

void loop() {
  touching = touch1.isPressed();
  Serial.println(touching);
  if (touching){
    evshield.bank_a.motorRunUnlimited(SH_Motor_Both, SH_Direction_Reverse, SH_Speed_Medium);
    
  } else {
    evshield.bank_a.motorStop(SH_Motor_Both, SH_Next_Action_BrakeHold);
  }
  delay(100);

}
