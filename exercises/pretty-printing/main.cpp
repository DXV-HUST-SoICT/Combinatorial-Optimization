#include <bits/stdc++.h>

using namespace std;

const int NMAX = 10000;
const int LMAX = 10000;

int n, L;
int c[NMAX];
int d[NMAX][LMAX];
int INF;

int sqr(int x) {
	return x * x;
}

int main() {
	cin >> n >> L;
	INF = 0;
	for (int i = 0; i < n; i++) {
		cin >> c[i];
		INF += c[i] + 1;
	}

	INF *= 10;

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j < L - c[i]; j++) {
			d[i][j] = INF;
		}
	}

	d[0][0] = 0;

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j < L - c[i]; j++) {
			d[i][j + c[i] + 1] = min(d[i][j + c[i] + 1], d[i - 1][j] - sqr(L - j) + sqr(L - (j - c[i] - 1)));
		}
		for  (int j = 0; j <= L; j++) {
			d[i][c[i]] = min(d[i][c[i]], d[i - 1][j]);
		}
		for (int j = c[i]; j <= L; j++) {
			d[i][0] = min(d[i][0], d[i][j] + sqr(L));
		}
	}

	int res = d[n][0];
	for (int j = 0; j <= L; j++) {
		res = min(res, d[n][j]);
	}

	cout << res << endl;

	return 0;
}