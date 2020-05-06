public class TestSimplex {
	public static void main(String[] args) {
		// double[][] a = new double[][] { {5, 15}, {4, 4}, {35, 20} };
		// double[] b = new double[] {480, 160, 1190};
		// double[] c = new double[] {13, 23};
		// double[][] a = new double[][] {{6, 0, 1, -1, 0}, {0, 4, 1, 1, 0}, {0, 0, -1, -1, 4}};
  //       double[] b = new double[] {6, 6, -2};
  //       double[] c = new double[] {0, 1, 0, 0, 0};
		// double[][] a = new double[][] {{3, 2}, {-3, 2}};
  //       double[] b = new double[] {6, 0};
  //       double[] c = new double[] {0, 1};
		double[][] a = new double[][] {{6, 0, 1, -1, 0}, {0, 4, 1, 1, 0}, {0, 1, 0, 0, 0}};
        double[] b = new double[] {6, 6, 1};
        double[] c = new double[] {0, 1, 0, 0, 0};
		Simplex s = new Simplex(a, b, c);
		s.solve();
		int m = s.getM();
		int n = s.getN();
		double[][] tmp = s.getA();
		System.out.println(-tmp[m][n + m]);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (tmp[j][i] != 0) {
					System.out.println(i + ": " + tmp[j][m + n] / tmp[j][i]);
				}
			}
		}
	}
}