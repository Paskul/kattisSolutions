import java.util.Scanner;

class goatRope {
    public static void main (String[] args) {
        int[] inputs = new int[6];
        Scanner scan = new Scanner(System.in);
        for(int i = 0; i < 6; i++) {
            inputs[i] = scan.nextInt();
        }
        scan.close();
        int postx = inputs[0];
        int posty = inputs[1];
        int x1 = inputs[2];
        int y1 = inputs[3];
        int x2 = inputs[4];
        int y2 = inputs[5];
        // System.out.println(Arrays.toString(inputs));
        // GIVEN that x2 > x1
        // GIVEN that y2 > y1
        //calculating x3,y3,x4, and y4
        //SHAPE IS GONNA LOOK LIKE
        // x3     x2
        //
        // x1     x4
        int x3 = x1;
        int y3 = y2;
        int x4 = x2;
        int y4 = y1;
        int[] listOfX = new int[] {x1, x2, x3, x4};
        int[] listOfY = new int[] {y1, y2, y3, y4};
        double runDistance = 0;
        double farthestCornerDistance = 0;
        for (int j = 0; j<4; j++) {
            runDistance = Math.pow((Math.pow(postx-listOfX[j], 2)) + (Math.pow(posty-listOfY[j], 2)), 0.5);
            // Could be an erorr here with conversion of int to double, if so turn points into doubles instead of ints
            if (runDistance > farthestCornerDistance) {
                farthestCornerDistance = runDistance;
            }
        }
        double shortestCornerDistance = farthestCornerDistance;
        int shortestCornerX = 0;
        int shortestCornerY = 0;
        // realize I can make it faster/efficent by storing the first set of data then comparing instead of 2 for loops
        for (int k = 0; k<4; k++) {
            runDistance = Math.pow((Math.pow(postx-listOfX[k], 2)) + (Math.pow(posty-listOfY[k], 2)), 0.5);
            if (runDistance < shortestCornerDistance) {
                shortestCornerDistance = runDistance;
                shortestCornerX = listOfX[k];
                shortestCornerY = listOfY[k];
            }
        }
        if ((x3 <= postx) && (postx <= x2)) {
            //System.out.println("thinks inbetween x3 and x2");
            if (posty > y3) {
                double printing = posty - y3;
                System.out.println(printing);
            }
            else {
                double printing2 = y1 - posty;
                System.out.println(printing2);
            }
        }
        else if ((y1 <= posty) && (posty <= y3)) {
            //System.out.println("thinks inbetween y1 and y3");
            if (postx > x2) {
                double printing3 = postx - x2;
                System.out.println(printing3);
            }
            else {
                double printing4 = x1 - postx;
                System.out.println(printing4);
            }
        }
        else {
            //System.out.println("returning corner distance");
            System.out.println(shortestCornerDistance);
        }
    }
}
