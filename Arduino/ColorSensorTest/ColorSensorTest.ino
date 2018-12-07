#define S0 4
#define S1 5
#define S2 6
#define S3 7
#define SENSOR_OUT 8

const int RED = 0;
const int GREEN = 1;
const int BLUE = 2;
const int CLEAR = 3;
const int NONE = 4;

// Stores frequency read by the photodiodes
int redFrequency = 0;
int greenFrequency = 0;
int blueFrequency = 0;

// Stores the red. green and blue colors
int redColor = 0;
int greenColor = 0;
int blueColor = 0;

char printBuff[50];
void setup() {
  Serial.begin(9600);
  Serial.println("Setting up pins...");

  Serial.print("Setting up colours");
  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);

  Serial.println("Setting up sensor output");
  pinMode(SENSOR_OUT, INPUT);

  Serial.println("Setting frequency scaling to 20%");
  digitalWrite(S0,HIGH);
  digitalWrite(S1,LOW);
  Serial.println("Done");
  
}

int getColorFreq(int c){
  int freq = 0;
  if (c == RED){
    Serial.print("RED ");
    digitalWrite(S2, LOW);
    digitalWrite(S3, LOW);
    freq = pulseIn(SENSOR_OUT, LOW);
  } else if (c == BLUE){
    Serial.print("BLUE ");
    digitalWrite(S2, LOW);
    digitalWrite(S3, HIGH);
    freq = pulseIn(SENSOR_OUT, LOW);
  } else if (c == GREEN){
    Serial.print("GREEN ");
    digitalWrite(S2, HIGH);
    digitalWrite(S3, HIGH);
    freq=pulseIn(SENSOR_OUT, LOW);
  } else if (c == CLEAR){
    Serial.print("CLEAR ");
    digitalWrite(S2, HIGH);
    digitalWrite(S3, LOW);
    freq=pulseIn(SENSOR_OUT, LOW);
  }
  return freq;
}

int getColor(int r, int g, int b){
  //red >50<60 , >20<30, 
  // green
  // blue
  // silver
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(100);
  redFrequency = getColorFreq(RED);
  greenFrequency = getColorFreq(GREEN);
  blueFrequency = getColorFreq(BLUE);
  sprintf(printBuff, "%d,%d,%d", redFrequency, greenFrequency, blueFrequency );
  Serial.println(printBuff);

}
