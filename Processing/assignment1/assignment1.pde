int balloons = 10;
int[] xlocs;
int[] ylocs;
int[] sizes;
color[] colours;

int drift;
int step;

void setup(){
  xlocs = new int[balloons];
  ylocs = new int[balloons];
  sizes = new int[balloons];
  colours = new color[balloons];
  drift = (int)random(5, 10);
  step = (int)random(5, 10);
  
  for (int i = 0; i<xlocs.length; i++){
    xlocs[i] = (int)random(0, width);
    ylocs[i] = height;
    sizes = (int)random
  }
}

void draw(){
  for (int i = 0; i < xlocs.length; i++){
    ellipse(xlocs[i], ylocs[i], 
  }
}