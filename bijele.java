import java.util.Scanner;

public class bijele {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        for (int i = 0; i<6; i++) {
            int input = scan.nextInt();
            if (i == 0) {
                System.out.print((1-input) + " ");
            }
            if (i == 1) {
                System.out.print((1-input) + " ");
            }
            if (i == 2) {
                System.out.print((2-input) + " ");
            }
            if (i == 3) {
                System.out.print((2-input) + " ");
            }
            if (i == 4) {
                System.out.print((2-input) + " ");
            }
            if (i == 5) {
                System.out.print((8-input));
            }
        }
        scan.close();
    }
}
