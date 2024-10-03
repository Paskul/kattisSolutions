import java.util.Scanner;

public class sibice {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int count = scan.nextInt();
        int width = scan.nextInt();
        int length = scan.nextInt();
        double hyp = Math.sqrt(Math.pow(width, 2) + Math.pow(length, 2));
        int testing;
        for (int i = 0; i<count; i++) {
            testing = scan.nextInt();
            if (testing <= hyp) {
                System.out.println("DA");
            }
            else {
                System.out.println("NE");
            }
        }
        scan.close();
    }
}
