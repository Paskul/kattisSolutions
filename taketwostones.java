import java.util.Scanner;

public class twostones {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int cases = scan.nextInt();
        if (cases%2 == 1) {
            System.out.println("Alice");
        }
        else {
            System.out.println("Bob");
        }
        scan.close();
    }
}
