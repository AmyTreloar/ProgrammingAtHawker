#include "Arduino.h"
int blinkPin = 7;
int buttonPin = 10;
int buttonState=0;
void setup(){
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);
  pinMode(blinkPin, OUTPUT);
}
void loop(){
  buttonState = digitalRead(buttonPin);
  if (buttonState == 1){
    Serial.println("on");
    digitalWrite(blinkPin, HIGH);
  } else {
    Serial.println("off");
    digitalWrite(blinkPin, LOW);
  }
}
