int timeUnit = 200;
int dash = timeUnit * 3;
int dot = timeUnit * 1;
int letterGap = timeUnit;
int wordGap = timeUnit * 6;

int delayTime;
int blinkLed = 13;

char letters[] = {'a','b','c','d', ' '};
char *symbols[] = {". -", "- . . .", "- . - .", "- . .", ' '};

String sentence = "ac dc";
void setup() {
  Serial.begin(9600);
  Serial.println("Setting project morse code");
  pinMode(blinkLed, OUTPUT);
  Serial.println("set up complete");
}

void message(String msg) {
  Serial.print(msg);
  Serial.println(" ");

  int i;
  for (i = 0; i < msg.length(); i++) {
    delayTime = 0;
    Serial.print(msg[i]);
    if (msg[i] == '.') {
      Serial.println(" dot");
      delayTime = dot;
    } else if (msg[i] == '-') {
      Serial.println(" dash");
      delayTime = dash;
    }
    Serial.print("ON");
    digitalWrite(blinkLed, HIGH);
    delay(delayTime);
    Serial.println(" OFF");
    digitalWrite(blinkLed, LOW);
    delay(letterGap);
  }

}

String convertToMorse(String s){
  // iterate through the letters of this string
  // check to see where in the letters[] this letter
  // capture the morse code from symbols[]
  String out = "";
  for (int i = 0; i < s.length(); i++){
    for (int j = 0; j < sizeof(letters) - 1; j++){
      if (s[i] == letters[j]){
        out += symbols[j];
      }
    }
    out+= ' ';
  }
  return out;
}

void loop() {
  String code = convertToMorse(sentence);
  message(code);
//  message("-_._-_.");
//  message("._-");
//  message("-_-");
  digitalWrite(blinkLed, LOW);
  delay(wordGap);
}
