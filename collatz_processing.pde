import java.util.*;
import java.util.function.Supplier;
import processing.pdf.*;

void setup(){
  noLoop();
  beginRecord(PDF, "wallpaper.pdf");
  fullScreen();
  background(29, 27, 27);
  stroke(236, 77, 55, 2);
  strokeWeight(2);
  translate(height, width/2);
}

//global series;
List<Integer> series = new ArrayList<Integer>();
int lin = height/10;

void draw(){
  translate(height, width/2);
  for(int i = 1; i <= 10000; i++){
    collatz(i);
    Collections.reverse(series);
    //Iterator j = series.iterator();
    //(Integer)j.next()
    for(int j = 0; j < series.size(); j++){
      if(isEven(series.get(j))){
        rotate(0.12);
        line(0,0,0,-lin);
        translate(0, -lin);
      }else{
        rotate(-0.12);
        line(0,0,0,-lin);
        translate(0, -lin);
      }
    }
    resetMatrix();
    series.removeAll(series);
    translate(height, width/2);
  }
  endRecord();
}

boolean isEven(int number){
  if(number%2 == 0){
    return true;
  }else if(number%2 == 1){
    return false;
  }
  return false;
}

List<Integer> collatz(int number){
  while(number != 1){
    series.add(number);
    if (isEven(number)){
      number = number/2;
    }else{
      number = (3*number + 1)/2;
    }
  }
  series.add(1);
  return series;
}
