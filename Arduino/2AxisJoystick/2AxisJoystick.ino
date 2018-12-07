int joyButtonPin = 7;
int joyXInput = A0;
int joyYInput = A1;

int joyButtonValue = 0;
int joyXValue = 0;
int joyYValue = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("Setting up controller...");
  pinMode(joyButtonPin, INPUT);
  pinMode(joyXInput, INPUT);
  pinMode(joyYInput, INPUT);
  Serial.println("Setup complete...");
}

void loop() {
  // put your main code here, to run repeatedly:
  joyButtonValue = digitalRead(joyButtonPin);
  joyXValue = analogRead(joyXInput);
  joyYValue = analogRead(joyYInput);
  Serial.print("X "+joyXValue);
  
}
