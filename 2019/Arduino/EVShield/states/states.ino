//STATEs as a global variable
//use all capitals for states
const int FIND = 0;
const int FOLLOW = 1;
const int AVOID = 2



int lightThreshold = 70;
int darkThreshold = 30;

int STATE = FIND;

int findLine(int lineReading){
  if (lineReading >= darkThreshold){
    return FOLLOW;
  }
  evshield.bank_a.motorRunUnlimited(SH_Motor_Both, SH_Direction_Forward, SH_Speed_Medium);
  evshield.bank_b.motorRunUnlimited(SH_Motor_Both, SH_Direction_Forward, SH_Speed_Medium);
  return FIND;
}

void loop() {
  lineReading = lightSensor.getVal();
  promity = distance.getDist()

  if (STATE == FIND){
    STATE = findLine(lineReading);
  } else if (STATE == FOLLOW){
    STATE = followLine(lineReading, proximity);
  } else if (STATE == AVOID) {
    STATE = avoidThing(proximity);
  }

}
