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
    if (ypos[i] <= 0) {
      xpos[i] = (int)random(0, width);
      ypos[i] = height;
      riseSpeeds[i] = (int)random(2, 8);
      driftSpeeds[i] = (int)random(2, 8);
      colors[i] = color(random(0, 255), random(0, 255), random(0, 255));
      sizes[i] = (int)random(50, 150);
    }
    ellipse(xpos[i], ypos[i], sizes[i], sizes[i]);
    
    if  (xpos[i]<0+sizes[i]){
      ellipse(xpos[i]+width, ypos[i], sizes[i], sizes[i]);
    } else if (xpos[i]>width-sizes[i]){
      ellipse(xpos[i]-width, ypos[i], sizes[i], sizes[i]);
    }
    
    if (xpos[i] < 0){ 
      xpos[i] = width;
    } else if (xpos[i] > width){
      xpos[i] = 0;
    }
    
    if (directions[MOVE_UP] && directions[MOVE_DOWN]) {
      ypos[i] -= riseSpeeds[i];
    } else if (directions[MOVE_UP]) {
      ypos[i] -= riseSpeeds[i]*2;
    } else if (directions[MOVE_DOWN]) {
      ypos[i] -= riseSpeeds[i]/2;
    } else {
      ypos[i] -= riseSpeeds[i];
    }
    
    if (directions[MOVE_LEFT] && directions[MOVE_RIGHT]) {
    } else if (directions[MOVE_LEFT]) {
      xpos[i] -= driftSpeeds[i];
    } else if (directions[MOVE_RIGHT]) {
      xpos[i] += driftSpeeds[i];
    } 
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