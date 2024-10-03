import java.util.Scanner;

public class smil {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String line = scan.nextLine();
        scan.close();
        for (int i=0; i< line.length() ; i++) {
            if ((String.valueOf(line.charAt(i)).equals(":") || (String.valueOf(line.charAt(i)).equals(";"))) && (line.length()-(i) > 1)) {
                if (String.valueOf(line.charAt(i+1)).equals(")")) {
                    System.out.println(i);
                }
                else if (String.valueOf(line.charAt(i+1)).equals("-") && (line.length()-(i+1) > 1)) {
                    if (String.valueOf(line.charAt(i+2)).equals(")")) {
                        System.out.println(i);
                    }
                }
            }
        }
    }
}
