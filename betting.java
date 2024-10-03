import java.util.Scanner;

public class betting {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int input = scan.nextInt();
        scan.close();
        double num = 100.0 - (double)input;
        // first output
        System.out.println((num/input) + 1);
        // second output
        System.out.println((input/num) + 1);
    }
}
