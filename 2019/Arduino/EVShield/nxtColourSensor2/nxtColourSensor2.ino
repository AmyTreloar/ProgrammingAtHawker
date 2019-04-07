#include <EVShield.h>
#include <EVs_NXTColor.h>

EVShield     evshield(0x34,0x36);
EVs_NXTColor colorSensor;
int colourValue;
void setup() {
    Serial.begin(9600);
    Serial.println("------------------------------");
    Serial.println("Starting NXT Color Sensor Test");
    Serial.println("------------------------------");

    evshield.init(SH_HardwareI2C );
    colorSensor.init(&evshield, SH_BAS1);
    colorSensor.setType(SH_Type_COLORFULL);

    Serial.println ("Press GO button to continue");
    evshield.waitForButtonPress(BTN_GO);
}
int value; 
void loop() {
    colourValue = colorSensor.readColor();
    value = colorSensor.readValue();
    Serial.print("Color sensor : "); Serial.print(colourValue);
    Serial.print(" ,Colour Value :"); Serial.println(value);
    delayMicroseconds(40);
}
