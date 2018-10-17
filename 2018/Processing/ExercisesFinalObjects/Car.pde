class Car{
  float w;
  float h;
  float x; 
  float y;
  color c;
  int speed;
  boolean moveRight;
  Car(){
    w = 69; 
    h = w/2;
    x = random(0, width);
    y = 100;
    speed = (int)random(1, 10);
    int rnd = (int)random(1, 2); 
  }
}