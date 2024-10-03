import java.util.Scanner;

class exam {
    public static void main (String[] args) {
        String[] strings = new String[2];
        Scanner scan = new Scanner(System.in);
        int friendCorrect = scan.nextInt();
        scan.nextLine();
        for(int j = 0; j < 2; j++) {
            strings[j] = scan.nextLine();
        }
        scan.close();
        int match = 0;
        for (int i = 0; i < strings[0].length(); i++) {
            if (strings[0].charAt(i) == strings[1].charAt(i)) {
                match++;
            }
        }
        if (match > friendCorrect) {
            System.out.println(friendCorrect + (strings[0].length() - match));
        }
        else {
            System.out.println(match + (strings[0].length() - friendCorrect));
        }
    }
}
