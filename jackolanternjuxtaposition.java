import java.util.Scanner;

public class jackolanternjuxtaposition {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = 1;
        while (scan.hasNext()) {
            num = num*(scan.nextInt());
        }
        scan.close();
        System.out.println(num);
    }
}
