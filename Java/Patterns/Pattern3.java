package Java.Patterns;


/**
 * Pattern:
 *    A   
 *   ABA  
 *  ABCBA
 * ABCDCBA
 */
public class Pattern3 {
    public static void main(String[] args) {
        int n=4;
        Pattern3 pattern3 = new Pattern3();
        pattern3.pattern(n);
    }

    public void pattern(int n) {
        for(int i=0; i<n; i++) {
            // Spaces
            for(int j=0; j<n-i-1; j++){
                System.out.print(" ");
            }
            // Forward order characters
            for(int j=0; j<=i; j++){
                System.out.print((char)(65+j));
            }
            // Reverse order characters
            for(int j=i-1; j>=0; j--){
                System.out.print((char)(65+j));
            }
            System.out.println();
        }
    }
}
