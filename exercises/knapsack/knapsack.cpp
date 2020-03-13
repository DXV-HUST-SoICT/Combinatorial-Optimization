#include <bits/stdc++.h>

using namespace std;

const int NMAX = 10000;
const int KMAX = 10000;

int n, k;
int w[NMAX], v[NMAX];
int c[NMAX][KMAX];
int s[NMAX][KMAX];
int res;
int rs[NMAX];

int maxValue(int l, int r) {
	if (l < 0) {
		return 0;
	}
	if (r < 0) {
		return 0;
	}
	if (c[l][r] < 0) {
		if (r >= w[l]) {
			c[l][r] = maxValue(l - 1, r - w[l]) + v[l];
			s[l][r] = 1;
		} else {
			s[l][r] = 0;
		}
		int tmp = maxValue(l - 1, r);
		if (tmp > c[l][r]) {
			c[l][r] = tmp;
			s[l][r] = 0;
		}
	}
	return c[l][r];
}

int main() {
	freopen("knapsack.txt", "r", stdin);
	cin >> n >> k;
	for (int i = 1; i <= n; i++) {
		cin >> w[i] >> v[i];
	}
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= k; j++) {
			c[i][j] = -1;
		}
	}
	for (int i = 0; i <= n; i++) {
		c[i][0] = 0;
	}
	for (int j = 1; j <= k; j++) {
		c[0][j] = 0;
	}
	cout << maxValue(n, k) << endl;
	int tmp_n = n;
	int tmp_k = k;
	while (tmp_n > 0) {
		if (s[tmp_n][tmp_k]) {
			rs[tmp_n] = 1;
			tmp_k -= w[n];
		} else {
			rs[tmp_n] = 0;
		}
		tmp_n--;
	}
	for (int i = 1; i <= n; i++) {
		cout << rs[i] << ' ';
	}
	cout << endl;
	return 0;
}