#include <IRremote.h>

int buttonState = 0; 
int buttonPin = 2;
int RECV_PIN = 11; 
IRrecv irrecv(RECV_PIN);
decode_results results;

class EngineController{
  int forward;
  int backward;
  int enable;
  int speed;
  String id;
  public:
  EngineController(int e, int f, int b, String i){
    id = i;
    enable = e;
    forward = f;
    backward = b;
    speed = 255;
    pinMode(forward, OUTPUT);
    pinMode(backward, OUTPUT);
    pinMode(enable, OUTPUT);
    Serial.print(id);
    Serial.println(" ready");
  }
  void goForwards(){
    Serial.print(id);
    Serial.println(" forward...");
    analogWrite(enable, speed);
    digitalWrite(forward, HIGH);
    digitalWrite(backward, LOW);
  }
  
  void goBackwards(){
    Serial.print(id);
    Serial.println(" backwards...");
    analogWrite(enable, speed);
    digitalWrite(forward, LOW);
    digitalWrite(backward, HIGH);
  }
  
  void stop(){
    analogWrite(enable, 0);
    digitalWrite(forward, LOW);
    digitalWrite(backward, LOW);
  }
};

EngineController rumble = EngineController(3, 4, 5, "Rumble motor");

void setup(){
  Serial.begin(9600);
  Serial.println("Initialising board...");
  pinMode(buttonPin, INPUT);
  irrecv.enableIRIn();
  Serial.println("Done!");
}

void loop(){
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {
    rumble.goForwards();
    if (irrecv.decode(&results)){
      Serial.println(results.value, HEX);
      irrecv.resume();
    }
  } else {
    rumble.stop();
  }
  delayMicroseconds(100);
}
