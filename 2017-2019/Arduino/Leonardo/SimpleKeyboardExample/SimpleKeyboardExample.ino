// Setting up constant variables as pin addresses
const int buttonPin = 12;  // my button
const int switchPin = 2;   // switch between keyboard and serial

// Storing the basic state of the system
int keyboardState;         // If this is true, I am in keyboard. Otherwise serial
int keystate;              // if this is pressed send my key
void setup()
{
  Serial.begin(9600);
  Serial.println("Setting up...");
  pinMode(buttonPin, INPUT);
  pinMode(switchPin, INPUT);
}

void setKeyboardState(int kbstate){
  if (kbstate){
    Keyboard.begin();
  } else {
    Keyboard.end();
  }
}

void loop(){
  keyboardState = digitalRead(switchPin)
  setKeyboardState(keyboardState);
  if (!keyboardState) continue;

  if (buttonPin){
    Keyboard.write('a');
  }
  
  delayMicroseconds(100);
}
