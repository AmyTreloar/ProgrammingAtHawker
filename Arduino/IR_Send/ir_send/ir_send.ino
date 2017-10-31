#include <IRremote.h>
int LED_PIN = 13; 
IRsend irsend;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  Serial.println("Sending");
  for (int i = 0; i < 3; i++){
    irsend.sendSony(0xa90, 12);
    delay(40);
  }
  Serial.println("sent");
  digitalWrite(LED_PIN, LOW);
  delay(1000);
  digitalWrite(LED_PIN, HIGH);
}
