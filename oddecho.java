import java.util.Scanner;

public class oddecho {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int wordCount = scan.nextInt();
        String curWord;
        for (int i = 0; i<=wordCount; i++) {
            curWord = scan.nextLine();
            if (i%2==1) {
                System.out.println(curWord);
            }
        }
        scan.close();
    }
}
