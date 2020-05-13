import java.io.FileInputStream;
import java.util.Scanner;

public class GomoryTwoPhaseSimplex {
	protected Fraction[][] tbl;
	protected boolean[] integral;  // = true if i-th variable must be integral
	protected int n;
	protected int m;
	protected Fraction[] result;
	protected int N;
	protected int M;

	public GomoryTwoPhaseSimplex(Fraction[][] tbl, boolean[] integral) {
		M = m = tbl.length - 1;
		N = n = tbl[0].length - 1;
		this.tbl = new Fraction[m + 1][n + 1];
		for (int i = 0; i <= m; i++) {
			for (int j = 0; j <= n; j++) {
				this.tbl[i][j] = new Fraction(tbl[i][j]);
			}
		}
		
		this.integral = new boolean[n];
		for (int j = 0; j < n; j++) {
            this.integral[j] = integral[j];
        }

        this.result = new Fraction[n];
	}

	public int twoPhaseSimplex(int count) {
		System.out.println("Loop " + count + ":");
		System.out.println("==> initial");
		printTableaux();
		TwoPhaseSimplex solver = new TwoPhaseSimplex(tbl);
		if (!solver.solve()) {
			System.out.println("Can't solve LP problem");
			return -1;
		}
		Fraction[][] tbl = solver.getTbl();
		int[] b = solver.getB();

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
		this.tbl = tmp_tbl;
		m += 1;
		n += 1;

		System.out.println("End loop " + count + "!");
		return 0;
	}

	public boolean solve() {
		int count = 0;
		while (true) {
			count++;
			int res = twoPhaseSimplex(count);
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
			fileName = "data/gomory_04";
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

			GomoryTwoPhaseSimplex solver = new GomoryTwoPhaseSimplex(tbl, integral);
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

	public Fraction[] getResult() {
		return result;
	}

	public void printTableaux() {
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				System.out.print(tbl[i][j] + "\t");
			}
			System.out.println(" | " + tbl[i][n]);
		}

		for (int j = 0; j < n; j++) {
			System.out.print(tbl[m][j] + "\t");
		}
		System.out.println(" | " + tbl[m][n]);
		System.out.println("======");
	}

	public void printTableaux(Fraction[][] tbl, int[] b) {
		int m = tbl.length - 1;
		int n = tbl[0].length - 1;
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
		System.out.println("======");
	}

	public Fraction[][] getTbl() {
		return tbl;
	}
}