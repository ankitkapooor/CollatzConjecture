import java.util.*;
import java.util.function.Supplier;

public class Collatz{
  static List<Integer> series = new ArrayList<Integer>();
  public static int collatz(int number){
    series.add(number);
    if(number != 1){
      if(number%2 == 0){
        number = number/2;
        collatz(number);
      }else if(number%2 == 1){
        number = 3*number + 1;
        collatz(number);
      }
    }
  return 0;
  }

  public static void main(String[] args){
    int number = 10000;
    for(int i = 1; i < number; i++){
      collatz(i);
      System.out.println(series.toString());
      series.removeAll(series);
    }
  }
}
