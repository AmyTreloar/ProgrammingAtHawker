#include <SoftI2cMaster.h>
#include <SHDefines.h>
#include <MsTimer2.h>
#include <EVs_SumoEyes.h>
#include <EVs_RTC.h>
#include <EVs_PSPNx.h>
#include <EVs_PiLight.h>
#include <EVs_PFMate.h>
#include <EVs_NXTVoltMeter.h>
#include <EVs_NXTTouch.h>
#include <EVs_NXTThermometer.h>
#include <EVs_NXTServo.h>
#include <EVs_NXTMMX.h>
#include <EVs_NXTLight.h>
#include <EVs_NXTCurrentMeter.h>
#include <EVs_NXTColor.h>
#include <EVs_NXTCam.h>
#include <EVs_NumericPad.h>
#include <EVs_MagicWand.h>
#include <EVs_LineLeader.h>
#include <EVs_LightSensorArray.h>
#include <EVs_IRThermometer.h>
#include <EVs_EV3Ultrasonic.h>
#include <EVs_EV3Touch.h>
#include <EVs_EV3SensorMux.h>
#include <EVs_EV3Infrared.h>
#include <EVs_EV3Gyro.h>
#include <EVs_EV3Color.h>
#include <EVs_DISTNx.h>
#include <EVs_AngleSensor.h>
#include <EVs_AbsoluteIMU.h>
#include <EVShieldUART.h>
#include <EVShieldI2C.h>
#include <EVShieldAGS.h>
#include <BaseI2CDevice.h>
#include <Wire.h>
#include <EVShield.h>



/*
 Name:		RoboGuy.ino
 Created:	11/9/2017 5:47:07 PM
 Author:	Adam Carter
*/

EVShield evshield;
EVs_EV3Infrared dist1;

// the setup function runs once when you press reset or power the board
void setup() {
	Serial.begin(115200);
	delay(500);
	Serial.println("Initialising device...");

	evshield.init(SH_HardwareI2C);

	Serial.println("Press Go to continue...");
	while (!evshield.getButtonState(BTN_GO)) {
		if (millis() % 1000 < 3) {
			Serial.print(".");
			delay(100);
		}

		dist1.init(&evshield, SH_BAS1);
		evshield.bank_a.motorReset();
		evshield.bank_b.motorReset();
	}
	Serial.println("Init complete");
}

int a; 
char str[256];
bool touch_status;
bool last_status;

// the loop function runs over and over again until power down or reset
void loop() {
	//a = touch1.readRaw();
	//touch_status = touch1.isPressed();
	//sprintf(str, "touch1: is pressed: %s", touch_status ? "true" : "false");
	/**Serial.println(str);
	if (touch_status != last_status) {
		Serial.println("Run unlimited");
		evshield.bank_a.motorRunUnlimited(SH_Motor_1, SH_Direction_Forward, 100);
	}
	else {
		Serial.println("Stop");
		evshield.bank_a.motorStop(SH_Motor_1, SH_Next_Action_Float);
	}
	last_status = touch_status;**/
	Serial.println(dist1.readProximity());
	delay(100);
}

