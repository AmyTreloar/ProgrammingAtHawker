#include <Keyboard.h>
int buttonPin = 2;
int playPin = 3;
int ledPin = 13;
int buttonState = LOW;
int playState = 1;
boolean playing = true;

int triggerX = 6;
int echoX = 7;
int triggerY = 8;
int echoY = 9;

class GameInterface{
  unsigned long prevDistance = 0;
  unsigned long prevTime = 0;
  boolean xAxis;
  int dtime = 500; 
  public:
  GameInterface(boolean leftAndRight){
    xAxis = leftAndRight;
  }

  void test(unsigned long distance){
    unsigned long currTime = millis();
    if (currTime < prevTime + dtime){
      return;
    }
    if (distance > 100) return;
    if (prevDistance - distance < 5) return; 
    if (distance - prevDistance < 5) return;
    Serial.print(xAxis);
    Serial.print(" ");
    Serial.print(prevDistance);
    Serial.print(" ");
    Serial.print(distance);
    Serial.print(" ");
    Serial.print(distance > prevDistance);
    Keyboard.begin();
    delayMicroseconds(100);
    if (distance > prevDistance){
      Serial.println("-----");
      if (xAxis) Keyboard.write(211);
      else Keyboard.write(217);
    } else {
      Serial.println("+++++");
      if (xAxis) Keyboard.write(' ');//Keyboard.write(214);
      else Keyboard.write(218);
    }
    Keyboard.releaseAll();
    delayMicroseconds(100);
    Keyboard.end();
    prevTime = currTime; 
    prevDistance = distance; 
    
  }
};

unsigned long ping(int triggerPin, int echoPin){
  unsigned long duration;
  unsigned long distance;
  pinMode(triggerPin, OUTPUT);
  digitalWrite(triggerPin, HIGH);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration/2)/29;
  //Serial.print(" ");
  //Serial.print(distance);
  //Serial.print(" ");
  return distance; 
}

GameInterface updown = GameInterface(false);
GameInterface leftright = GameInterface(true);
void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(playPin, INPUT_PULLUP);
  Serial.begin(9600);
  //Keyboard.begin();
}

//todo back  211
//todo next  214
//

void goNext(){
  //Keyboard.write('a');
}

void goBack(){
  //Keyboard.write(211);
}

void loop() {
  /*Serial.print(millis());
  Serial.print(" ");
  Serial.println(playing);
  */
  if (!playing) return;
  playState = digitalRead(playPin);
  if (playState == HIGH){
    playing = false;
    Serial.println("game over");
    return;
  } 
  // put your main code here, to run repeatedly:
  buttonState = digitalRead(buttonPin);
  //Serial.print("Button ");
  //Serial.print(buttonState);
  updown.test(ping(triggerY, echoY));
  leftright.test(ping(triggerX, echoX));
  //Serial.println("");
  Keyboard.releaseAll();
  delayMicroseconds(100);
}
