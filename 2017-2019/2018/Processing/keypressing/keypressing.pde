// 2. make ball that we can move around the
//    the screen with wasd

int x;
int y;
int d;
int step;

void setup(){
  size(800, 600);
  x = width/2;
  y = height/2;
  d = 100;
  step = 5;
}

void draw() {
  background(255);
  fill(0);
  ellipse(x, y, d, d );
}

void keyPressed(){
  if (key == 'w'){
     y = y - step;
  } else if (key == 's') {
    y = y + step;
  }
}