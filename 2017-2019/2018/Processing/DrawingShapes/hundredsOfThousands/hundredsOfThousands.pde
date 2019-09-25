void setup(){
  size(800, 600);
}

void draw(){
  background(255);
  for (int i = 0; i < 100000; i++){
    fill(random(0, 255), random(0, 255), random(0, 255));
    ellipse(random(0, width), random(0, height), random(5, 20), random(5, 20));
  }
}