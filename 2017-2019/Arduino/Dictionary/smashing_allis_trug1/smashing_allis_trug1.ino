
typedef struct {
  char* letter;
  char* symbol;
} symLookup;

const symLookup morseCode[27] {
  {"a", ".-"},
  {"b", "-..."},
  {"c", "-.-."},
  {"d", "-.."},
  {"e", "."},
  {"f", "..-."},
  {"g", "-.-."},
  {"h", "...."}, 
  {"i", ".."},  
  {"j", ".---"},
  {"k", "-.-"},  
  {"l", ".-.."},  
  {"m", "--"},  
  {"n", "-."},  
  {"o", "---"},  
  {"p", ".--."},  
  {"q", "--.-"},  
  {"r", ".-."},  
  {"s", "..."},  
  {"t", "-"},
  {"u", "..-"},
  {"v", "...-"},
  {"w", ".--"},
  {"x", "-..-"},
  {"y", "-.--"},
  {"z", "--.."},
  {" ", "     "},
};


int unit = 400;
int dot = unit;
int dash = 3*unit;
int symbol = unit;
int letter = 2*unit;
int space = 6*unit;

char name[] = "adam carter";
int sig = 13;
char* symbols; 

void setup()
{
  Serial.begin(9600);
  Serial.println("Starting ...");
  pinMode(sig, OUTPUT);
  Serial.println("init complete");
}

char* getSymbolFromLetter(char letter){
  //I made a hash map
  for (int i = 0; i < sizeof(morseCode); i++){
    if(letter == morseCode[i].letter[0]){
      Serial.print(letter);
      return morseCode[i].symbol;
    }
  }
  return 0;
}

/** 
 void beep will flash a light for a defined period of time and then
 turn the light off. It will then delay for one time u nit. 
*/
void beep(int d){
  digitalWrite(sig, HIGH);
  delay(d);
  digitalWrite(sig, LOW);
  delay(symbol);
}

void sendWord(char n[], int size){
  //At first glance you would think I could use 
  //sizeof(name) but I can't. 
  //This is due to how C++ passes references to items
  
  for (int i = 0; i<size;i++){
    // for every character in the name
    symbols = getSymbolFromLetter(n[i]); // get thet symbol
    Serial.println(symbols); //write them for us to see
    
    for (int j = 0; j < sizeof(symbols); j++){ // for every symbol
      if (symbols[j] == '-'){ 
        beep(dash);
      } else if (symbols[j] == '.'){
        beep(dot);
      } else if (symbols[j] == ' '){
        beep(space);
      }
    }
  }
}

void loop()
{
  int nameSize = sizeof(name);
  /* 
    I need to pass both the name and it's size to my helper function
    because C++ is anti social 
  */
  sendWord(name, nameSize); 
  
}
