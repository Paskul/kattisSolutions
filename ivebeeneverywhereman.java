import java.util.ArrayList;
import java.util.Scanner;

public class everywhere {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int testCases = scan.nextInt();
        for (int i = 0; i < testCases; i++) {
            int curTrips = scan.nextInt();
            ArrayList<String> cities = new ArrayList<String>();
            for (int j = 0; j <= curTrips; j++) {
                cities.add(scan.nextLine());
            }
            cities = removeDuplicates(cities);
            System.out.println(cities.size()-1);
        }
    }
    public static <T> ArrayList<T> removeDuplicates(ArrayList<T> list) {
        ArrayList<T> newList = new ArrayList<T>();
  
        for (T element : list) {
  
            // If this element is not present in newList
            // then add it
            if (!newList.contains(element)) {
  
                newList.add(element);
            }
        }
  
        // return the new list
        return newList;
    }
}
