import java.io.FileInputStream;
import java.util.Scanner;

public class GomoryDualSimplex extends GomoryTwoPhaseSimplex {
//    protected int[] b;
    public GomoryDualSimplex(Fraction[][] tbl, boolean[] integral) {
        super(tbl, integral);
    }

    @Override
    public boolean solve() {
        int count = 0;
        int res = twoPhaseSimplex(count);
        if (res == -1) {
            return false;
        } else if (res == 1) {
            return true;
        }

        while (true) {
            count++;
            res = dualSimplex(count);
            if (res == -1) {
                return false;
            } else if (res == 1) {
                break;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        String fileName = "";
        if (args.length > 0) {
            fileName = args[0];
        } else {
            fileName = "data/gomory_02";
        }
        try {
            FileInputStream fis = new FileInputStream(fileName);
            Scanner s = new Scanner(fis);
            int m = s.nextInt();	// No constraints
            int n = s.nextInt();	// No variables

            Fraction[][] tbl = new Fraction[m+1][n+1];  // Simplex Tableaux
            // Last row: objective function
            // Last column: value
            for (int i = 0; i < m; i++) {
                for (int j = 0; j <= n; j++) {
                    tbl[i][j] = new Fraction(s.nextDouble());
                }
            }


            for (int j = 0; j < n; j++) {
                tbl[m][j] = new Fraction(s.nextDouble());
            }

            tbl[m][n] = new Fraction(0);

            boolean[] integral = new boolean[n];

            for (int j = 0; j < n; j++) {
                integral[j] = false;
            }

            int ni = s.nextInt();
            for (int i = 0; i < ni; i++) {
                integral[s.nextInt()] = true;
            }

            GomoryDualSimplex solver = new GomoryDualSimplex(tbl, integral);
            if (solver.solve()) {
                Fraction[] result = solver.getResult();
                for (int i = 0; i < n; i++) {
                    System.out.println("x[" + i + "] = " + result[i]);
                }
            }
        }
        catch(Exception e) {
            e.printStackTrace();
        }
    }

    public int dualSimplex(int count) {
        System.out.println("Loop " + count + ":");
        System.out.println("==> initial");
        printTableaux();
        DualSimplex solver = new DualSimplex(tbl, b);
        if (!solver.solve()) {
            System.out.println("Can't solve LP problem");
            return -1;
        }
        Fraction[][] tbl = solver.getTbl();
        this.b = solver.getB();

        for (int i = 0; i < N; i++) {
            result[i] = new Fraction(0);
        }

        int p = -1;
        for (int i = 0; i < m; i++) {
            if (b[i] >= N) {
                continue;
            }
            result[b[i]] = tbl[i][n].divide(tbl[i][b[i]]);
            if ((integral[b[i]] == true) && (result[b[i]].getDenominator() != 1)) {
                p = i;
                break;
            }
        }
        if (p == -1) {
            return 1;
        }

        Fraction[][] tmp_tbl = new Fraction[m + 2][n + 2];

        tmp_tbl[m + 1][n] = new Fraction(0);
        tmp_tbl[m + 1][n + 1] = new Fraction(this.tbl[m][n]);
        for (int j = 0; j < n; j++) {
            tmp_tbl[m + 1][j] = new Fraction(this.tbl[m][j]);
        }

        tmp_tbl[m][n] = new Fraction(-1, 1);
        tmp_tbl[m][n + 1] = tbl[p][n].minus(tbl[p][n].floor());

        for (int j = 0; j < n; j++) {
            tmp_tbl[m][j] = tbl[p][j].minus(tbl[p][j].floor());
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                tmp_tbl[i][j] = new Fraction(tbl[i][j]);
            }
            tmp_tbl[i][n] = new Fraction(0);
            tmp_tbl[i][n + 1] = new Fraction(tbl[i][n]);
        }

        int[] tmp_b = new int[m + 1];
        for (int i = 0; i < b.length; i++) {
            tmp_b[i] = b[i];
        }
        tmp_b[m] = n;

        this.tbl = tmp_tbl;
        this.b = tmp_b;
        m += 1;
        n += 1;

        System.out.println("End loop " + count + "!");
        return 0;
    }
}
