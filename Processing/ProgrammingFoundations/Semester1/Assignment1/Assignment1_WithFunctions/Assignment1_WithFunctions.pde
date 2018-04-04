// setting up some variable names that mean numbers so I can refference different parts of my directions
// array below. 
static int MOVE_UP = 0; 
static int MOVE_DOWN = 1;
static int MOVE_LEFT = 2;
static int MOVE_RIGHT = 3;
boolean[] directions = new boolean[4];

int numBalloons = 10;  // the number of balloons. 

/** 
 * Each array holds one component of a balloon. 
 * For instance, xpos holds all of the x positions and ypos holds the y positions. 
 */
int[] xpos = new int[numBalloons];
int[] ypos = new int[numBalloons];
int[] sizes = new int[numBalloons];
int[] riseSpeeds = new int[numBalloons];
int[] driftSpeeds = new int[numBalloons];
color[] colors = new color[numBalloons];



void setup() {
  size(800, 600);
}

void draw() {
  background(255);
  for (int i = 0; i<numBalloons; i++) {
    fill(colors[i]);
    checkPop(i);
    drawBalloons(xpos[i], ypos[i], sizes[i]);
    xpos[i] = checkSideBoundaries(xpos[i]);

    ypos[i] -= rise(riseSpeeds[i]);
    xpos[i] += drift(driftSpeeds[i]);
  }
}

/**
* draws main balloon and a proxy balloon if requried
*/
void drawBalloons(int x, int y, int s) {
  ellipse(x, y, s, s);

  if  (x<0+s) {
    ellipse(x+width, y, s, s);
  } else if (x>width-s) {
    ellipse(x-width, y, s, s);
  }
}

/**
* if the balloon hits the top of the screen it "pops"
*/
void checkPop(int i) {
  if (ypos[i] <= 0) {
    xpos[i] = (int)random(0, width);
    ypos[i] = height;
    riseSpeeds[i] = (int)random(2, 8);
    driftSpeeds[i] = (int)random(2, 8);
    colors[i] = color(random(0, 255), random(0, 255), random(0, 255));
    sizes[i] = (int)random(50, 150);
  }
}

/**
* checks to see if the centre of the balloon has exited either side of the boundary window
*/
int checkSideBoundaries(int x) {
  if (x < 0) {
    return width;
  }
  if (x > width) {
    return 0;
  }
  return x;
}

/** 
* moves the balloon up. 
*/
int rise(int speed) {
  if (directions[MOVE_UP] && !directions[MOVE_DOWN]) {
    return speed*2;
  }  
  if (directions[MOVE_DOWN] && !directions[MOVE_UP]) {
    return speed/2;
  } 
  return speed;
}

int drift(int speed) {
  if (directions[MOVE_LEFT] && !directions[MOVE_RIGHT]) {
    return  -speed;
  } 
  if (directions[MOVE_RIGHT] && !directions[MOVE_LEFT]) {
    return speed;
  }
  return 0;
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