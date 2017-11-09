#include <Wire.h>
#include <EVShield.h>
#include <EVs_NXTTouch.h>

EVShield evshield;

EVs_NXTTouch touch1;

void setup() {
  Serial.begin(115200);
  delay(500);
  Serial.println("Initializing device...");

  evshield.init(SH_HardwareI2C);

  while (!evshield.getButtonState(BTN_GO)){
    if  (millis() % 1000 < 3) {
      Serial.println("Press GO button to continue...");
      delayMicroseconds(100);
    }
  }

  touch1.init(&evshield, SH_BAS1);

  evshield.bank_a.motorReset();
  evshield.bank_b.motorReset();

}

void loop() {
  char aa[80];
  int a;
  char str[256];
  bool touch_status;
  bool last_status;

  while (true) {
    a = touch1.readRaw();
    touch_status = touch1.isPressed();
    sprintf(str, "touch1: is pressed: %s", touch_status?"true":"false");
    Serial.println(str);
    
    if (touch_status != last_status) {
      if (touch_status){
        Serial.println("Run unlimited");
        evshield.bank_a.motorRunUnlimited(SH_Motor_1, SH_Direction_Forward, 100);
      } else {
        Serial.println("stop (float)");
        evshield.bank_a.motorStop(SH_Motor_1, SH_Next_Action_Float);
      }

      last_status = touch_status;
    }
    
    delay(500);
  }

}
