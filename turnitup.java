import java.util.Scanner;

public class skruop {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int count = scan.nextInt();
        int volume = 7;
        String request = "";
        for (int i = 0; i<=count; i++) {
            request = scan.nextLine();
            if ((request.length() == 8) && (volume < 10)) {
                volume = volume + 1;
            }
            else if ((request.length() == 9) && (volume > 0)) {
                volume = volume - 1;
            }
        }
        scan.close();
        System.out.println(volume);
    }
}
