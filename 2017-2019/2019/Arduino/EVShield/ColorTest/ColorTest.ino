#include <BaseI2CDevice.h>
#include <EVShield.h>
#include <EVShieldAGS.h>
#include <EVShieldI2C.h>
#include <EVShieldUART.h>
#include <EVs_AbsoluteIMU.h>
#include <EVs_AngleSensor.h>
#include <EVs_DISTNx.h>
#include <EVs_EV3Color.h>
#include <EVs_EV3Gyro.h>
#include <EVs_EV3Infrared.h>
#include <EVs_EV3SensorMux.h>
#include <EVs_EV3Touch.h>
#include <EVs_EV3Ultrasonic.h>
#include <EVs_IRThermometer.h>
#include <EVs_LightSensorArray.h>
#include <EVs_LineLeader.h>
#include <EVs_MagicWand.h>
#include <EVs_NumericPad.h>
#include <EVs_NXTCam.h>
#include <EVs_NXTColor.h>
#include <EVs_NXTCurrentMeter.h>
#include <EVs_NXTLight.h>
#include <EVs_NXTMMX.h>
#include <EVs_NXTServo.h>
#include <EVs_NXTThermometer.h>
#include <EVs_NXTTouch.h>
#include <EVs_NXTVoltMeter.h>
#include <EVs_PFMate.h>
#include <EVs_PSPNx.h>
#include <EVs_RTC.h>
#include <EVs_SumoEyes.h>
#include <MsTimer2.h>
#include <SHDefines.h>
#include <SoftI2cMaster.h>

//#include <EVShield.h>
//#include <EVs_EV3Color.h>

EVShield     evshield(0x34,0x36);
EVs_EV3Color colorSensor; 
int colorDetected;

void setup(){

    Serial.begin(9600);
    Serial.println ("--------------------------------------");
    Serial.println ("EV3 Colour Sensor Test");
    Serial.println ("--------------------------------------");

    evshield.init( SH_HardwareI2C );
    colorSensor.init( &evshield, SH_BAS1 );
    colorSensor.setMode(MODE_Color_MeasureColor);

    Serial.println ("Press GO button to continue");
    evshield.waitForButtonPress(BTN_GO);

}

void loop(){
    colorDetected = colorSensor.getVal();
    Serial.print("Colour value: "); 
    Serial.println(colorDetected);
    delay(500);
}
