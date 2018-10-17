int number = 10;
int xPos[] = new int[number];
int yPos[] = new int[number];
int stepX[] = new int[number];
int stepY[] = new int[number];

void setup(){
  //size(600, 200);
  fullScreen();
  fill(0);
  for (int i = 0; i < number; i++){
    xPos[i] = (int)random(0, width);
    yPos[i] = (int)random(0, height);
    stepX[i] = 5;
    stepY[i] = -5;
  }
}

void draw(){
  background(255);
  for (int i = 0; i < number; i++){
    xPos[i] = xPos[i] +stepX[i];
    yPos[i] = yPos[i] + stepY[i];
    ellipse(xPos[i], yPos[i], 20, 20);
    if (xPos[i] > width || xPos[i] < 0){
      stepX[i] = 0 - stepX[i];
    }
    
    if (yPos[i] > height || yPos[i] < 0){
      stepY[i] = 0 - stepY[i];
    }
  }
}