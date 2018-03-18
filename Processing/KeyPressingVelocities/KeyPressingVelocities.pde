float vel;
float x;
float y;
float step;

void setup() {
  vel = 1;
  x = 0;
  y = width/2;
  step = 2;
  size(600, 400);
}

void draw() {
  background(255);
  rect(x, y, 40, 40); 
  x = x+(step * vel);
  if (x > width) x = 0;
}

void keyPressed() {
  if (key == CODED) {
    if (keyCode == RIGHT) {
      vel = 2;
    } else if (keyCode == LEFT) {
      vel = 0.5;
    }
  }
}

void keyReleased() {
  if (key == CODED) {
    if (keyCode == RIGHT) {
      vel = 1;
    } else if (keyCode == LEFT) {
      vel = 1;
    }
  }
}