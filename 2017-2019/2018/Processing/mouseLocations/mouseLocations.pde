int circleX;
int circleY;
int radius; 

void setup(){
  size(800, 600);
  radius = 20;
}

void draw() {
  background(255);
  circleX = mouseX; 
  circleY = mouseY;
  
  if (circleX < width/2) {
    if (circleY < height/2) {
      fill(255);
    } else {
      fill(255, 0, 0);
    }
  } else {
    if (circleY < height/2) { 
      fill(0, 255, 0);
    } else {
      fill(0, 0, 255);
    }
  }
  
  ellipse(circleX, circleY, radius, radius);
}