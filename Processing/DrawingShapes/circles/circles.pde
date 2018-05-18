void setup() {
  size(640, 480);
}

void draw() {
  fill(color(255, 0, 0));
  ellipse(mouseX, mouseY, 50, 50);
  fill(color(255, 204, 0));
  ellipse(mouseX+15, mouseY+15, 50, 50);
  fill(color(255, 0, 0));
  ellipse(mouseX-15, mouseY+15, 50, 50);
}