#include "Keyboard.h"
#include "Mouse.h"
 
boolean running;

void setup() {
  Serial.begin(9600);
  pinMode(2, INPUT_PULLUP);
  running = false;
}

void loop() {
  while (digitalRead(2) == HIGH){
    if (running == true) {
      running = false;
    //Keyboard.end();
      Serial.println("Keyboard ending");
    }
    Serial.print(".");
    delay(500);
  }
  if (running == false) {
    running = true;
    Serial.println("Keyboard starting");
    //Keyboard.begin();
  }
  Serial.println("key press");
  //Keyboard.press('Q');
  delay(100);

}
