public  class Simplex 
{
    private double [][] a; //simplex tableaux
    private int M, N;
    
    public Simplex (double [][] A, double [] b, double [] c)
    {
        M = b.length;
        N = c.length;
        a = new double[M+1][M+N+1];
        for(int i=0; i < M; i++)
            for (int j = 0; j < N; j++)
                a[i][j] = A[i][j];
        for (int j = N; j < M + N; j++) a[j-N][j] = 1.0;
        for (int j = 0; j < N;     j++) a[M][j] = c[j];
        for (int i = 0; i < M;     i++) a[i][M+N] = b[i];
    }
    public void pivot(int p, int q)
    {
        for (int i = 0; i <= M; i++)
            for (int j = 0; j <= M + N; j++)
                if (i != p && j != q)
                    a[i][j] -= a[p][j] * a[i][q] / a[p][q];
        for (int i = 0; i <= M; i++)
            if (i != p) a[i][q] = 0.0;
        for (int j=0; j <= M + N; j++)
            if (j != q) a[p][j] /= a[p][q];
        a[p][q] = 1.0;
    }
    public void solve ()
    {
        while (true)
        {
            int p, q;
            for (q = 0; q < M + N; q++)
                if (a[M][q] > 0) break;
            if (q >= M + N) break;

            for (p = 0; p < M; p++)
                if (a[p][q] > 0) break;
            for (int i=p+1; i < M; i++)
                if (a[i][q] > 0)
                    if (a[i][M+N] / a[i][q] < a[p][M+N] / a[p][q])
                    p = i;
            pivot(p,q);
        }
    }
}