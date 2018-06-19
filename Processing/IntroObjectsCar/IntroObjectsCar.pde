Car[] myCars;

void setup() {
  size(800, 600);
  myCars = new Car[1];
  for (int i = 0; i < myCars.length; i++){
    myCars[i] = new Car();
  }
}

void draw() {
  background(255);
  for (int i = 0; i < myCars.length; i++){
    myCars[i].drive(); 
    myCars[i].display();
  }
}