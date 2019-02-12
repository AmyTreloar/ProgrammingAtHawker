void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Hello world");
  delay(100);
  Serial.print(".");
  delay(100);
  Serial.print(".");
  delay(100);
  Serial.println(".");
}
