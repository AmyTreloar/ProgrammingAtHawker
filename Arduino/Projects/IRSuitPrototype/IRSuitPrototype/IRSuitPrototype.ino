#include <IRremote.h>

int powerPin = 13; 
IRsend irsend;


void setup() {
  // put your setup code here, to run once:
  pinMode(powerPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("debugging");
}

void loop() {
  Serial.println("Sending");
  
  for (int i = 0; i < 3; i++){
    irsend.sendSony(0xa90, 12);
    delay(40);
  }
  Serial.println("sent");
  delay(1000);
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  
  
}
