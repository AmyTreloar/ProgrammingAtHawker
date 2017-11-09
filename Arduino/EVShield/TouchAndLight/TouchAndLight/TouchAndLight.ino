#include <Wire.h>
#include <EVShield.h>
#include <EVs_NXTTouch.h>
#include <EVs_NXTLight.h>

EVShield evshield;

EVs_NXTTouch touch1;
EVs_NXTLight light1;
bool lastTouch, touchPressed;

void setup() {
  Serial.begin(115200);
  delay(500);
  Serial.println("Initializing device...");
  evshield.init(SH_HardwareI2C);

  Serial.println("Press GO button to continue");
  evshield.waitForButtonPress(BTN_GO);

  touch1.init(&evshield, SH_BAS1);
  light1.init(&evshield, SH_BAS2);
  

}

void loop() {
  char str[256];
  int lightReading; 
  Serial.println("into loop --------");

  touchPressed = touch1.isPressed();
  sprintf(str, "Touch1: is pressed: %s", touchPressed?"true":"false");
  Serial.println(str);

  if (touchPressed != lastTouch){
    if (touchPressed == true) {
      Serial.println("Changing light sensor to reflect light mode");
      //light1.setActive();
      light1.setReflected();
    } else {
      Serial.println("Changing light sensor to ambient light mode");
      //light1.setPassive();
      light1.setAmbient();
    }
    lightReading = light1.readRaw();
    sprintf(str, "Light sensor reading: %d", lightReading);
    Serial.println(str);
    delay(500);
  }

}
