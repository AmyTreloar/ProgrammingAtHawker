void setup()
{
  Serial.begin(9600);
  Serial.println("Enter the servo name and pin number");
  Serial.println("Format: [name]:[pin]");
  Serial.println("e.g.,: 'servo1:9'");
}

void loop()
{
}

void serialEvent(){
  String servo = Serial.readStringUntil(':');
  int pin = Serial.readString().toInt();
  Serial.println(servo+" "+pin); 
}
