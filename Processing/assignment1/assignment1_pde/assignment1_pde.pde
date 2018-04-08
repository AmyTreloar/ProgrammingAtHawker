class Balloon{
  int x; 
  int y; 
  int riseSpeed;
  int driftSpeed;
  color c;
  int size;
  
  Balloon(){
    setBalloon();
  }
  
  void setBalloon(){
    x = (int) random(0, width);
    y = height;
    riseSpeed = (int) random(1, 10);
    driftSpeed = (int) random(1, 10);
    c = color(random(0, 255), random(0, 255), random(0, 255));
    size = (int)random(80, 180);
  }
  int moveSideways(int xpos, int xvel){
    int newX = xpos; 
    if (xpos > width){
      xpos = 0; 
    } else if (xpos < 0) {
      xpos = width;
    }
    
    if (xvel > 0){
      newX = xpos + driftSpeed;
    } else if (xvel < 0){
      newX = xpos - driftSpeed;
    }
    return newX;
  }
  int moveUp(int ypos, int yvel){
    int newY = y - riseSpeed; 
    if (ypos <=0 ){
      setBalloon();
      newY = height;
    }
    if (yvel > 0) {
       newY = ypos - (riseSpeed * 2);
    }
    
    if (yvel < 0) {
      newY = ypos - (riseSpeed / 2);
    }
    
    return newY; 
  }
  public void update(int xvel, int yvel){
    y = this.moveUp(y,  yvel);
    x = this.moveSideways(x, xvel);
    fill(c);
    ellipse(x, y, size, size);
  }
}

int numOfBalloons = 100;
int  xVelocity = 0;
int  yVelocity = 0; 

Balloon[] balloons = new Balloon[numOfBalloons];

void setup(){
  fullScreen();
  //size(1024, 768);
  for (int i = 0; i < balloons.length; i++){
    balloons[i] = new Balloon();
  }
}

void draw(){
  background(255);
  for (int i = 0; i < balloons.length; i++){
    balloons[i].update(xVelocity, yVelocity);
  }
}

void keyPressed(){
  if (key != CODED) return;
  if (keyCode == LEFT){
    println("left is pressed");
    xVelocity = -1; 
  } else if (keyCode == RIGHT){
    xVelocity = 1;
  }
  
  if (keyCode == UP){
    println("UP is pressed");
    yVelocity = -1;
  } else if (keyCode == DOWN){
    yVelocity = 1;
  }
}

void keyReleased() { 
  if (key != CODED) return;
  if (keyCode == LEFT){
    println("left is released");
    xVelocity = 0; 
  } else if (keyCode == RIGHT){
    xVelocity = 0;
  }
  
  if (keyCode == UP){
    println("UP is released");
    yVelocity = 0;
  } else if (keyCode == DOWN){
    yVelocity = 0;
  }
}