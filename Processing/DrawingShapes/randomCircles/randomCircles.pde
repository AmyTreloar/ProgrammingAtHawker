float[] sizes = new float[4];

void setup(){
  for (int i = 0; i < sizes.length; i++){
    sizes[i] = random(5, 20);
  }
}

void draw(){
  for (int i = 0; i < sizes.length; i++){
    ellipse(20 + 20*i, 20 + 20*i, sizes[i], sizes[i]); 
  }
}