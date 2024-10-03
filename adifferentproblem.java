import java.math.BigInteger;
import java.util.Scanner;
public class different {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        while (scan.hasNext()) {
            String num1 = scan.next();
            String num2 = scan.next();
            
            BigInteger first = new BigInteger(num1);
            BigInteger second = new BigInteger(num2);
            
            System.out.println((first.subtract(second)).abs());
        }
        scan.close();
    }
}
