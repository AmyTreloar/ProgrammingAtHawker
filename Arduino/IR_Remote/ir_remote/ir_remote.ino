#include <IRremote.h>

int RECV_PIN = 11; 


IRrecv irrecv(RECV_PIN);

IRsend irsend;

//FD58A7
decode_results results;

void setup(){
  Serial.begin(9600);
  Serial.println("Enabling IRin");
  irrecv.enableIRIn();
  Serial.println("Enabled IRin");
}

void loop(){
  if (irrecv.decode(&results)){
    Serial.println(results.value, HEX);
    irrecv.resume();
  }
  delay(100);
}

