package Java.Patterns;

/**
 * Program to print the following pattern:
 * 1      1
 * 12    21
 * 123  321
 * 12344321
 * 
 */

public class Pattern1 {
    public static void main(String[] args) {
        int n = 9; // Number of rows
        printPattern(n);

    }

    public static void printPattern(int n) {
        for (int i = 1; i <= n; i++) {
            // Print left side numbers
            for (int j = 1; j<=i; j++){
                System.out.print(j);
            }
            // Print spaces 
            for (int j = 0; j<2*n-2*i; j++) {
                System.out.print(" ");
            }
            // Print right side numbers

            for (int j=i; j>0; j--){
                System.out.print(j);
            }
            System.out.println();
        }
        return;
    }
}
