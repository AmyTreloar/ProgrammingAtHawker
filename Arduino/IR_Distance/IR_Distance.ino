#define reading A0
unsigned int value;
char str[256];
void setup(){
  pinMode(reading, INPUT);
  Serial.begin(9600);
  Serial.println("Value \r Voltage");
}


void loop(){
  value = analogRead(reading);  
  Serial.println(value);
  delay(100);
}

