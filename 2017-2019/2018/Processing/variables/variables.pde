
int box_width = 100;
int box_height = 100;

void setup(){
  size(640, 480);
}

void draw() {
  //background(255);
  fill(255, 0, 0);
  rect(mouseX - box_width/2, mouseY - box_height/2, box_width, box_height);
  fill(0, 255,0);
  rect(mouseX, mouseY, box_width, box_height);
  fill(0, 0, 255);
  rect(mouseX - box_width, mouseY - box_height, box_width, box_height);
}