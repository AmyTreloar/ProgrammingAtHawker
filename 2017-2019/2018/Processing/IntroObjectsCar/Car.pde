class Car{
  int x;
  int y;
  int speed;
  color c;
  int carHeight;
  int carLength;
  
  Car(){
    this.carHeight = 15;
    this.carLength = 50;
    this.x = 0;
    this.y = (int)random(0, height);
    this.speed = (int)random(1,2);
    this.c = color(
      random(0, 255),
      random(0, 255),
      random(0, 255)
    );
  }
  Car(int x, int y, int speed, color c){
    this.x = x;
    this.y = y;
    this.speed = speed;
    this.c = c;
  }
  
  void display(){
    fill(c);
    rect(x, y, carLength, carHeight);
    fill(0);
    ellipse(x+10, y+carHeight, 10, 10);
    ellipse(x+carLength-10, y+carHeight, 10, 10);
    
    //cabin (rect)
  }
  
  void drive(){
    x = x + speed;
    if (x > width) {
      x = 0;
    }
  }
}