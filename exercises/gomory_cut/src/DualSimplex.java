class DualSimplex extends Simplex {
    public DualSimplex(Fraction[][] tbl, int[] b) {
        super(tbl, b);
    }

    @Override
    public boolean solve() {
        System.out.println("==> Solving Dual:");
        if (!solveDual()) {
            return false;
        }
        System.out.println("====> Dual Solution:");
        printTableaux();

        System.out.println("==> Solving Primal:");
        if (!super.solve()) {
            return false;
        }
        System.out.println("====> Primal Solution");
        printTableaux();
        return true;
    }

    public static void main(String[] args) {

    }

    public boolean solveDual() {
        this.standardize();
        boolean solvable;
        while (true) {
            int p, q;
            for (p = 0; p < m; p++) {
                if (tbl[p][n].compare(0) < 0) {
                    break;
                }
            }
            if (p >= m) {
                solvable = true;
                break;
            }

            for (q = 0; q < n; q++) {
                if (tbl[p][q].compare(0) < 0) {
                    break;
                }
            }
            if (q >= n) {
                solvable = false;
                break;
            }
            for (int i = q + 1; i < n; i++) {
                if (tbl[p][i].compare(0) < 0) {
                    if (tbl[m][i].divide(tbl[p][i]).compare(tbl[m][q].divide(tbl[p][q])) < 0) {
                        q = i;
                    }
                }
            }
            pivot(p, q);
            printTableaux();
        }
        return solvable;
    }
}