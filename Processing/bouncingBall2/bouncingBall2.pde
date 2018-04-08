// 1 make a ball that can bounce of the left
//   and right walls

// 2. make ball that we can move around the
//    the screen with wasd

// 3. make a ball that appears at the bottom
//    and travels up to the top screen while
//    moving side to side.
//    when we get  to the top we respawn at
//    the bottom

int x;
int y;
int r;
int step;
boolean moveRight;

void setup(){
  size(800, 600);
  x = width/2;
  y = height/2;
  r = 100;
  moveRight = true;
  step = 5;
}

void draw() {
  println(x);
  background(250);
  fill(0);
  ellipse(x,y,r,r);
  if (moveRight) {
    x = x + step;
  } else {
    x = x - step;
  }
  
  if (x > width-r/2) {
    moveRight = false;
  }
  if (x <= 0+r/2) {
    moveRight = true;
  }
}