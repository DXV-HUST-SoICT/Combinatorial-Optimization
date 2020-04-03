public  class Simplex 
{
    private double [][] a; //simplex tableaux
    private int m, n;

    public double[][] getA() {
        return a;
    }

    public int getM() {
        return this.m;
    }

    public int getN() {
        return this.n;
    }
    
    public Simplex (double [][] A, double [] b, double [] c)
    {
        m = b.length;
        n = c.length;
        a = new double[m+1][m+n+1];
        for(int i=0; i < m; i++)
            for (int j = 0; j < n; j++)
                a[i][j] = A[i][j];
        for (int j = n; j < m + n; j++) a[j-n][j] = 1.0;
        for (int j = 0; j < n;     j++) a[m][j] = c[j];
        for (int i = 0; i < m;     i++) a[i][m+n] = b[i];
    }
    public void pivot(int p, int q)
    {
        for (int i = 0; i <= m; i++)
            for (int j = 0; j <= m + n; j++)
                if (i != p && j != q)
                    a[i][j] -= a[p][j] * a[i][q] / a[p][q];
        for (int i = 0; i <= m; i++)
            if (i != p) a[i][q] = 0.0;
        for (int j=0; j <= m + n; j++)
            if (j != q) a[p][j] /= a[p][q];
        a[p][q] = 1.0;
    }
    public void solve ()
    {
        while (true)
        {
            int p, q;
            for (q = 0; q < m + n; q++)
                if (a[m][q] > 0) break;
            if (q >= m + n) break;

            for (p = 0; p < m; p++)
                if (a[p][q] > 0) break;
            for (int i=p+1; i < m; i++)
                if (a[i][q] > 0)
                    if (a[i][m+n] / a[i][q] < a[p][m+n] / a[p][q])
                    p = i;
            pivot(p,q);
        }
    }
}