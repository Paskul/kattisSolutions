import java.util.Scanner;

public class autori {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String line = scan.nextLine();
        scan.close();
        String result = (String.valueOf(line.charAt(0)));
        for (int i = 0; i<line.length(); i++) {
            if (String.valueOf(line.charAt(i)).equals("-")) {
                result = (result + (String.valueOf(line.charAt(i+1))));
            }
        }
        System.out.println(result);
    }
}
