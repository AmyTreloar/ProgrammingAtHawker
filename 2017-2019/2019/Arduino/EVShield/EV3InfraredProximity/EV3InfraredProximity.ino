// Attach EV3 Infrared Sensor to Port BAS1
// Open the Serial terminal to view results.

#include <Wire.h>
#include <EVShield.h>
#include <EVShieldAGS.h>
#include <EVs_EV3Infrared.h>

EVShield        evshield(0x34,0x36);
EVs_EV3Infrared distance;

void setup() {

    Serial.begin(9600);

    Serial.println ("-----------------------------------------");
    Serial.println ("Starting EV3 Infrared Sensor Test Program");
    Serial.println ("-----------------------------------------");

    evshield.init( SH_HardwareI2C );
    distance.init( &evshield, SH_BAS1 );
    distance.setMode(MODE_Infrared_Proximity);

    Serial.println ("Press GO button to continue");
    evshield.waitForButtonPress(BTN_GO);

}
int proximity;
void loop() {
    proximity = distance.readProximity();
    Serial.print("Proximity: "); Serial.println(proximity);
    delayMicroseconds(200);
}
