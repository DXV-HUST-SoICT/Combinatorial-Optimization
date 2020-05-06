import java.io.FileInputStream;
import java.util.Scanner;

public class TwoPhaseSimplex {
	private Fraction[][] tbl;	// Simplex Tableaux (last row is objective function, last column is value)
	private int[] b;
	private int m;	// No constraints
	private int n;	// No variables

	public TwoPhaseSimplex(Fraction[][] tbl) {
		m = tbl.length - 1;
		n = tbl[0].length - 1;
		this.tbl = new Fraction[m + 1][n + 1];
		this.b = new int[m + 1];
		for (int i = 0; i <= m; i++) {
			for (int j = 0; j <= n; j++) {
				if (tbl[i][j] == null) {
					System.out.println(i + " " + j);
				}
				this.tbl[i][j] = new Fraction(tbl[i][j]);
			}
		}
	}

	// Find a basic feasible solution
	public boolean findBFS() {
		// Simplex tabular of prolem with slack variables
		Fraction[][] tbl = new Fraction[m+1][n+m+1];
		int[] b = new int[m];	// Base of constraint

		// Coefficients of actual variables
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				tbl[i][j] = new Fraction(this.tbl[i][j]);
			}
		}

		for (int i = 0; i < m; i++) {
			for (int j = n; j < n + m; j++) {
				tbl[i][j] = new Fraction(0, 1);
			}
			// Coefficients of slack variables
			tbl[i][n + i] = new Fraction(1, 1);
			// Values of equalities
			tbl[i][n + m] = new Fraction(this.tbl[i][n]);
			// Coefficients of objective funtion
			tbl[i][n + i] = new Fraction(1, 1);
			// Base of constraint is slack variable
			b[i] = n + i;
		}

		for (int j = 0; j < n; j++) {
			tbl[m][j] = new Fraction(0);
		}

		for (int j = n; j < m + n; j++) {
			tbl[m][j] = new Fraction(-1, 1);
		}

		tbl[m][n + m] = new Fraction(0);

		System.out.println("====> Fake BFS with slack variables");
		printTableaux(tbl, b);

		Simplex ss = new Simplex(tbl, b);
		if (!ss.solve()) {
			return false;
		}
		
		b = ss.getB();
		tbl = ss.getTbl();

		System.out.println("====> BFS with slack variables");
		printTableaux(tbl, b);

		if (tbl[m][n + m].compare(0) != 0) {
			System.out.println("BFS is not valid!");
			return false;
		}

		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				this.tbl[i][j] = tbl[i][j];
			}
			this.tbl[i][n] = tbl[i][n + m];
		}

		boolean[] flag = new boolean[n];
		for (int i = 0; i < n; i++) {
			flag[i] = false;
		}
		for (int i = 0; i < m; i++) {
			if (b[i] < n) {
				this.b[i] = b[i];
				flag[b[i]] = true;
			}
		}
		for (int i = 0; i < m; i++) {
			if (b[i] >= n) {
				for (int j = 0; j < n; j++) {
					if (!flag[j]) {
						this.b[i] = j;
						flag[j] = true;
						break;
					}
				}
			}
		}

		return true;
	}

	public boolean solve() {

		System.out.println("==> Finding initial BFS");

		if (!findBFS()) {
			System.out.println("Can't find any BFS!");
			return false;
		}

		System.out.println("==> Finding LP optimum solution");

		System.out.println("====> BFS with only origin variables");
		printTableaux(tbl, b);
	
		Simplex solver = new Simplex(this.tbl, this.b);
		if (!solver.solve()) {
			System.out.println("Can't solve LP problem (phase 2)!");
			return false;
		}

		Fraction[][] tbl = solver.getTbl();
		int[] b = solver.getB();
		for (int i = 0; i <= m; i++) {
			for (int j = 0; j <= n; j++) {
				this.tbl[i][j] = tbl[i][j];
			}
			this.tbl[i][n] = tbl[i][n];
		}
		for (int i = 0; i < m; i++) {
			this.b[i] = b[i];
		}

		System.out.println("====> LP optimum solution");
		printTableaux();
		
		return true;
	}

	public static void main(String[] args) {
		try {
			FileInputStream fis = new FileInputStream("data/twophase_01");
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
		
			TwoPhaseSimplex solver = new TwoPhaseSimplex(tbl);
			solver.solve();
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

	public int[] getB() {
		return b;
	}
}