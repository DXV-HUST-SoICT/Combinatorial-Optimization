import java.io.FileInputStream;
import java.util.Scanner;

public class Simplex {

    protected Fraction [][] tbl; // Simplex Tableaux
    protected int[] b; // Base of i-th constraint
    protected int m;  // No constraints
    protected int n;  // No variables

    public Fraction[][] getTbl() {
        return tbl;
    }

    public int[] getB() {
        return b;
    }
    
    public Simplex (Fraction[][] tbl, int[] b) {
        m = tbl.length - 1;
        n = tbl[0].length - 1;
        this.tbl = new Fraction[m + 1][n + 1];
        this.b = new int[m];
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                this.tbl[i][j] = new Fraction(tbl[i][j]);
            }
        }
        for (int i = 0; i < m; i++) {
            this.b[i] = b[i];
        }
    }

    public void pivot(int p, int q) {
        b[p] = q;
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i != p && j != q) {
                    tbl[i][j] = tbl[i][j].minus(tbl[p][j].multiply(tbl[i][q]).divide(tbl[p][q]));
                }
            }
        }
        for (int i = 0; i <= m; i++) {
            if (i != p) {
                tbl[i][q] = new Fraction(0, 1);
            }
        }
        for (int j=0; j <= n; j++) {
            if (j != q) {
                tbl[p][j] = tbl[p][j].divide(tbl[p][q]);
            }
        }
        tbl[p][q] = new Fraction(1, 1);
    }

    public boolean solve() {
        this.standardize();
        boolean solvable;
        while (true) {
            int p, q;
            for (q = 0; q < n; q++) {
                if (tbl[m][q].compare(0) > 0) {
                    break;
                }
            }
            if (q >= n) {
                solvable = true;
                break;
            }

            for (p = 0; p < m; p++) {
                if (tbl[p][q].compare(0) > 0) {
                    break;
                }
            }
            if (p >= m) {
                solvable = false;
                break;
            }
            for (int i = p + 1; i < m; i++) {
                if (tbl[i][q].compare(0) > 0) {
                    if (tbl[i][n].divide(tbl[i][q]).compare(tbl[p][n].divide(tbl[p][q])) < 0) {
                        p = i;
                    }
                }
            }
            pivot(p, q);
        }
        
        return solvable;
    }

    public void standardize() {

        // Basic coefficient = 1
        for (int i = 0; i < m; i++) {
            // System.out.println("Check: " + i + " " + b[i] + " " + n);
            Fraction c = tbl[i][b[i]];
            for (int j = 0; j <= n; j++) {
                tbl[i][j] = tbl[i][j].divide(c);
            }
        }

        for (int i = 0; i < m; i++) {
            Fraction c = tbl[m][b[i]].divide(tbl[i][b[i]]);
            for (int j = 0; j <= n; j++) {
                tbl[m][j] = tbl[m][j].minus(c.multiply(tbl[i][j]));
            }
        }
        System.out.println("====> Standardized");
        printTableaux();

    }

    public static void main(String[] args) {
        try {
            FileInputStream fis = new FileInputStream("data/simplex_01");
            Scanner s = new Scanner(fis);
            int m = s.nextInt();    // No constraints
            int n = s.nextInt();    // No variables

            Fraction[][] tbl = new Fraction[m+1][n+1];  // Simplex Tableaux 
                                                        // Last row: objective function
                                                        // Last column: value
            int[] b = new int[m];              // basic variable of i-th constraint
            for (int i = 0; i < m; i++) {
                for (int j = 0; j <= n; j++) {
                    tbl[i][j] = new Fraction(s.nextDouble());
                }
                b[i] = s.nextInt();
            }


            for (int j = 0; j < n; j++) {
                tbl[m][j] = new Fraction(s.nextDouble());
            }

            tbl[m][n] = new Fraction(0);
        
            Simplex solver = new Simplex(tbl, b);
            solver.solve();
            System.out.println(solver.getTbl()[m][n]);
        }
        catch(Exception e) {
            e.printStackTrace();
        }  
    }

    public void printTableaux() {
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(tbl[i][j] + "\t");
            }
            System.out.println(" | " + tbl[i][n] + "\tBase: " + b[i]);
        }

        for (int j = 0; j < n; j++) {
            System.out.print(tbl[m][j] + "\t");
        }
        System.out.println(" | " + tbl[m][n]);
        System.out.println();
    }
}