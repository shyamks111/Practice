package Java.Patterns;

/**
 * 
 * Pattern4
 * D
 * CD
 * BCD
 * ABCD
 */
public class Pattern4 {
    public static void main(String[] args) {
        int n=4;
        pattern(n);
    }

    public static void pattern(int n){
        for(int i=0; i<n; i++){
            for(int j=0; j<=i; j++){
                System.out.print((char)(65+n-1-i+j));
            }
            System.out.println();
        }

    }
}
