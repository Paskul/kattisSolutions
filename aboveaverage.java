import java.util.ArrayList;
import java.util.Scanner;

public class aboveaverage {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int cases = scan.nextInt();
        for (int i = 0; i<cases; i++) {
            ArrayList<Integer> curStudents = new ArrayList<Integer>();
            int students = scan.nextInt();
            double average = 0.0;
            double tally = 0.0;
            for (int k = 0; k<students; k++) {
                curStudents.add(scan.nextInt());
                average = average + (double)curStudents.get(k);
            }
            average = average/students;
            for (int j = 0; j<students; j++) {
                if ((double)curStudents.get(j) > average) {
                    tally = tally+1;
                }
            }
            tally = 100*(tally/students);
            System.out.printf("%.3f%% %n", tally);
        }
        scan.close();
    }
}
