// setting up some variable names that mean numbers so I can refference different parts of my directions
// array below. 
static int MOVE_UP = 0; 
static int MOVE_DOWN = 1;
static int MOVE_LEFT = 2;
static int MOVE_RIGHT = 3;
boolean[] directions = new boolean[4];

int numBalloons = 10;  // the number of balloons. 

Balloon[] balloons = new Balloon[numBalloons];

void setup() {
  size(800, 600);
  for (int i = 0; i < numBalloons; i++){
    balloons[i] = new Balloon();
  }
}

void draw() {
  background(255);
  for (int i = 0; i<numBalloons; i++) {
    balloons[i].update(directions);
  }
}

void keyPressed() {
  if (key == 'e' || key == 'E') {
    directions[MOVE_UP] = true;
  }
  if (key == 'd' || key == 'D') {
    directions[MOVE_DOWN] = true;
  }
  if (key == 'f' || key == 'F') {
    directions[MOVE_RIGHT] = true;
  }
  if (key == 's' || key == 'S') {
    directions[MOVE_LEFT] = true;
  }
}

void keyReleased() {
  if (key == 'e' || key == 'E') {
    directions[MOVE_UP] = false;
  }
  if (key == 'd' || key == 'D') {
    directions[MOVE_DOWN] = false;
  }
  if (key == 'f' || key == 'F') {
    directions[MOVE_RIGHT] = false;
  }
  if (key == 's' || key == 'S') {
    directions[MOVE_LEFT] = false;
  }
}