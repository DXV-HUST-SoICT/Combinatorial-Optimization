class DualSimplex extends Simplex {
    public DualSimplex(Fraction[][] tbl, int[] b) {
        super(tbl, b);
    }

    @Override
    public boolean solve() {
        this.standardize();
        if (!solveDual()) {
            return false;
        }
        if (!super.solve()) {
            return false;
        }
        return true;
    }

    public static void Main(String[] args) {

    }

    public boolean solveDual() {
        boolean solvable;
        while (true) {
            int p, q;
            for (p = 0; p < m; p++) {
                if (tbl[m][p].compare(0) > 0) {
                    break;
                }
            }
            if (p >= m) {
                solvable = true;
                break;
            }

            for (q = 0; q < n; q++) {
                if (tbl[p][q].compare(0) > 0) {
                    break;
                }
            }
            if (q >= n) {
                solvable = false;
                break;
            }
            for (int i = q + 1; i < n; i++) {
                if (tbl[p][i].compare(0) > 0) {
                    if (tbl[m][i].divide(tbl[p][i]).compare(tbl[m][q].divide(tbl[p][q])) < 0) {
                        q = i;
                    }
                }
            }
            pivot(p, q);
        }
        return solvable;
    }
}