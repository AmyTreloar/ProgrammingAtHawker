class Balloon {
  private int x; 
  private int y; 
  private int riseSpeed;
  private int driftSpeed;
  private color c;
  private int size;
  public Balloon() {
    spawn();
  }

  public void spawn() {
    this.x = (int)random(0, width);
    this.y = height;
    this.riseSpeed = (int)random(2, 8);
    this.driftSpeed = (int)random(2, 8);
    this.c = color(random(0, 255), random(0, 255), random(0, 255));
    this.size = (int)random(50, 150);
  }
  
  void update(boolean[] directions){
    if(checkPop()){
      spawn();
    }
    drawBalloons();
    this.y -= rise(directions);
    this.x += drift(directions);
  }

  void drawBalloons() {
    fill(c);
    ellipse(x, y, size, size);
    if  (x<0+size) {
      ellipse(x+width, y, size, size);
    } else if (x>width-size) {
      ellipse(x-width, y, size, size);
    }
  }

  /**
   * if the balloon hits the top of the screen it "pops"
   */
  boolean checkPop() {
    if (y <= 0) {
      return true;
    }
    return false;
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
  int rise(boolean[] directions) {
    if (directions[MOVE_UP] && !directions[MOVE_DOWN]) {
      return riseSpeed*2;
    }  
    if (directions[MOVE_DOWN] && !directions[MOVE_UP]) {
      return riseSpeed/2;
    } 
    return riseSpeed;
  }

  int drift(boolean[] directions) {
    if (directions[MOVE_LEFT] && !directions[MOVE_RIGHT]) {
      return  -driftSpeed;
    } 
    if (directions[MOVE_RIGHT] && !directions[MOVE_LEFT]) {
      return driftSpeed;
    }
    return 0;
  }
}