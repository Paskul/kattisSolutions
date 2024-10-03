import java.util.Scanner;

class nineKnights {
    public static void main (String[] args) {
        char[][] board = new char[5][5];
        int erorrs = 0;
        Scanner input = new Scanner(System.in);
        //char[][] board = new char[5][5];
        for (int i = 0; i < 5; i++) {
            String line = input.nextLine();
            for (int j = 0; j < 5; j++) {
                char curr = line.charAt(j);
                board[i][j] = curr;
            }
        }
        input.close();
        //System.out.println(Arrays.deepToString(board));
        int totalKnights = 0;
        boolean valid = true;
        for (int k = 0; k < 5; k++) {
            for (int h = 0; h < 5; h++) {
                try { 
                    if ((board[k-2][h-1]) == 'k' && (board[k][h]) == 'k')  {
                        valid = false;
                    }
                }
                catch(IndexOutOfBoundsException e) {
                    erorrs++;
                }
                try { 
                    if ((board[k-2][h+1]) == 'k' && (board[k][h]) == 'k') {
                        valid = false;
                    }
                }
                catch(IndexOutOfBoundsException e) {
                    erorrs++;
                }
                try { 
                    if ((board[k-1][h-2]) == 'k' && (board[k][h]) == 'k') {
                        valid = false;
                    }
                }
                catch(IndexOutOfBoundsException e) {
                    erorrs++;
                }
                try {
                    if ((board[k-1][h+2]) == 'k' && (board[k][h]) == 'k') {
                        valid = false;
                    }
                }
                catch(IndexOutOfBoundsException e) {
                    erorrs++;
                }
                try {
                    if ((board[k+1][h-2]) == 'k' && (board[k][h]) == 'k') {
                        valid = false;
                    }
                }
                catch(IndexOutOfBoundsException e) {
                    erorrs++;
                }
                try {
                    if ((board[k+1][h+2]) == 'k' && (board[k][h]) == 'k') {
                        valid = false;
                    }
                }
                catch(IndexOutOfBoundsException e) {
                    erorrs++;
                }
                try {
                    if ((board[k+2][h-1]) == 'k' && (board[k][h]) == 'k') {
                        valid = false;
                    }
                }
                catch(IndexOutOfBoundsException e) {
                    erorrs++;
                }
                try {
                    if ((board[k+2][h+1]) == 'k' && (board[k][h]) == 'k') {
                        valid = false;
                    }
                }
                catch(IndexOutOfBoundsException e) {
                    erorrs++;
                }
                finally {
                    if (valid != true) {
                        //System.out.println("invalid");
                        break;
                    }
                }
                if (board[k][h] == 'k') {
                    totalKnights++;
                }
                if (valid == false){
                    break;
                }
            }
            if (valid == false) {
                break;
            }
        }
        if (totalKnights != 9) {
            System.out.println("invalid");
        }
        else if(valid == true) {
            System.out.println("valid");
        }
        else {
            System.out.println("invalid");
        }
    }
}
