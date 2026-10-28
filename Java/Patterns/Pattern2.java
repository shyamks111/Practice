package Java.Patterns;

/**
 * Print the following pattern
 * 1
 * 2 3
 * 4 5 6
 * 7 8 9 10
 * 
 */

public class Pattern2 {
    
    public static void main(String[] args) {
        int n = 4;
        Pattern2 pattern2 = new Pattern2();
        pattern2.pattern(n);
    }

    public void pattern(int n) {
        
        int counter = 1;
        for (int i=0; i<n; i++) {
            for (int j=0; j<=i; j++){
                System.out.print(counter + " ");
                counter++;
            }
            System.out.println();
        }
    }
}
