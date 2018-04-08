int numberOfBalls = 1;
int[] xpos = new int[numberOfBalls];
boolean[] moveDirs = new boolean[2];

void setup(){
  size(800, 600);
  for (int i = 0; i < xpos.length; i++){
    xpos[i] = (int)random(0, width);
  }
}

void draw(){
  background(255);
  fill(255);
  for (int i = 0; i < xpos.length; i++){
    if (moveDirs[0] && moveDirs[1]) {
      // vel =1;
    } else if (moveDirs0) {
      // vel = 2;
      xpos[i] = xpos[i] - 5;
    } else if (moveDirs[1]){
      // vel = 0.5;
      xpos[i] = xpos[i] + 5;
    } else {
      //vel = 1;
    }
    ellipse(xpos[i], height/2, 40, 40);
  }
}

void keyPressed(){
  if (key == 's'){
    println("s is pressed");
    moveDirs[0] = true;
  } 
  if (key == 'f'){
    println("f is pressed");
    moveDirs[1] = true;
  }
}

void keyReleased(){
  if (key == 's'){
    println("s is released");
    moveDirs[0] = false;
  } 
  if (key == 'f'){
    println("f is released");
    moveDirs[1] = false;
  }
}