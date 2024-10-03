import java.util.Scanner;
import java.util.Arrays;

class pokerHand {
    public static void main (String[] args) {
        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine();
        scan.close();
        int[] firstChars = new int[]{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        int i = 0;
        while (i<input.length()) {
            if (input.charAt(i) == 'A') {
                firstChars[0] += 1;
            }
            if (input.charAt(i) == '2') {
                firstChars[1] += 1;
            }
            if (input.charAt(i) == '3') {
                firstChars[2] += 1;
            }
            if (input.charAt(i) == '4') {
                firstChars[3] += 1;
            }
            if (input.charAt(i) == '5') {
                firstChars[4] += 1;
            }
            if (input.charAt(i) == '6') {
                firstChars[5] += 1;
            }
            if (input.charAt(i) == '7') {
                firstChars[6] += 1;
            }
            if (input.charAt(i) == '8') {
                firstChars[7] += 1;
            }
            if (input.charAt(i) == '9') {
                firstChars[8] += 1;
            }
            if (input.charAt(i) == 'T') {
                firstChars[9] += 1;
            }
            if (input.charAt(i) == 'J') {
                firstChars[10] += 1;
            }
            if (input.charAt(i) == 'Q') {
                firstChars[11] += 1;
            }
            if (input.charAt(i) == 'K') {
                firstChars[12] += 1;
            }
            i += 3;
        }
        Arrays.sort(firstChars);
        System.out.println(firstChars[(firstChars.length-1)]);
    }
}
