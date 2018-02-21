int x; 
int y; 
int r; 
int step;
boolean stepRight; 

void setup(){
  size(800, 600);
  x = width/2;
  y = height/2;
  r = 80;
  step = 5; 
  stepRight = true;
}

void draw() {
  background(255);
  fill(255, 0, 0);
  ellipse(x, y, r, r);
  if (stepRight){
    x = x + 1;
  } else {
    x = x - 1;
  }
  if (x > width-r/2){
    stepRight = false;
  } else if (x < r/2){
    stepRight = true;
  }
}