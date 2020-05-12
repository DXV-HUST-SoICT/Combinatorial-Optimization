public class Fraction {
	private int numerator;
	private int denominator;

	public Fraction(int numerator, int denominator) {
		if (denominator == 0) {
			throw new RuntimeException("Denominator equals zero!");
		}
		this.numerator = numerator;
		this.denominator = denominator;
		this.reduce();
	}

	public Fraction(Fraction other) {
		this(other.getNumerator(), other.getDenominator());
	}

	public Fraction(double value) {
		double eps = 1e-10;
		int denominator = 1;
		while (Math.abs(value - (int) value) > 1e-10) {
			value *= 10;
			denominator *= 10;
		}
		int numerator = (int) value;
		this.numerator = numerator;
		this.denominator = denominator;
		this.reduce();
	}

	public int gcd(int a, int b) {
		int c = a % b;
		while (c != 0) {
			a = b;
			b = c;
			c = a % b;
		}
		return b;
	}

	public void reduce() {
		if (denominator < 0) {
			numerator = -numerator;
			denominator = -denominator;
		}
		int r = gcd(Math.abs(numerator), denominator);
		numerator /= r;
		denominator /= r;
	}

	public String toString() {
		if (denominator == 1) {
			return Integer.toString(numerator);
		} else {
			return Integer.toString(numerator) + "/" + Integer.toString(denominator);
		}
	}

	public int getNumerator() {
		return numerator;
	}

	public int getDenominator() {
		return denominator;
	}

	public Fraction plus(Fraction other) {
		int numerator = this.numerator * other.denominator + other.numerator * this.denominator;
		int denominator = this.denominator * other.denominator;
		return new Fraction(numerator, denominator);
	}

	public Fraction minus(Fraction other) {
		int numerator = this.numerator * other.denominator - other.numerator * this.denominator;
		int denominator = this.denominator * other.denominator;
		return new Fraction(numerator, denominator);
	}

	public Fraction negative() {
		int numerator = -this.numerator;
		int denominator = this.denominator;
		return new Fraction(numerator, denominator);
	}

	public Fraction multiply(Fraction other) {
		int numerator = this.numerator * other.numerator;
		int denominator = this.denominator * other.denominator;
		return new Fraction(numerator, denominator);
	}

	public Fraction divide(Fraction other) {
		int numerator = this.numerator * other.denominator;
		int denominator = this.denominator * other.numerator;
		return new Fraction(numerator, denominator);
	}

	public Fraction floor() {
		int delta = Math.abs(this.numerator) % this.denominator;
		int denominator = this.denominator;
		int numerator;
		if (delta == 0) {
			numerator = this.numerator;
		} else if (this.numerator > 0) {
			numerator = this.numerator - delta;
		} else {
			numerator = this.numerator - denominator + delta;
		}
		return new Fraction(numerator, denominator);
	}

	public Fraction ceil() {
		int delta = Math.abs(this.numerator) % this.denominator;
		int denominator = this.denominator;
		int numerator;
		if (delta == 0) {
			numerator = this.numerator;
		} else if (this.numerator > 0) {
			numerator = this.numerator + denominator - delta;
		} else {
			numerator = this.numerator + delta;
		}
		return new Fraction(numerator, denominator);
	}

	public int compare(Fraction other) {
		return this.numerator * other.denominator - other.numerator * this.denominator;
	}

	public int compare(int value) {
		Fraction other = new Fraction(value, 1);
		return this.compare(other);
	}

	public static void main(String[] args) {
		Fraction a = new Fraction(4, 8);
		Fraction b = new Fraction(2, 3);
		System.out.println(a.plus(b));
		System.out.println(a.minus(b));
		System.out.println(a.multiply(b));
		System.out.println(a.divide(b));
		System.out.println(a.negative());
		System.out.println(new Fraction(1.2));
	}
}