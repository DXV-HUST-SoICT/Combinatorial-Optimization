#include <bits/stdc++.h>

using namespace std;

const int NMAX = 20;

int n;
int a[NMAX][NMAX];
// c[i][j]: cost
// trang thai (i, j): bieu dien i duoi dang nhi phan, cac bit 1 tuong ung voi cac dinh da tham, j la dinh cuoi cung duoc tham
// p[i][j] = k: trang thai truoc (trang thai (i', k): i' la i nhung da tat bit thu j)
int c[1 << NMAX][NMAX];
int p[1 << NMAX][NMAX];
int inf = 0;
int res;
int rs[NMAX];

int minCost(int mask, int last) {
	if (!((mask >> last) & 1)) {
		return inf;
	}
	if ((mask != 1) && (last == 0)) {
		return inf;
	}
	if (c[mask][last] == inf) {
		int tmpMask = mask & ~(1 << last);
		for (int i = 0; i < n; i++) {
			if (i != last && ((tmpMask >> i) & 1)) {
				int tmp = minCost(tmpMask, i) + a[i][last];
				if (tmp < c[mask][last]) {
					c[mask][last] = tmp;
					p[mask][last] = i;
				}
			}
		}
	}
	return c[mask][last];
}

int main() {
	freopen("tsp.txt", "r", stdin);
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> a[i][j];
			inf += a[i][j];
		}
	}
	inf *= 2;

	int N  = (1 << n);

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < n; j++) {
			c[i][j] = inf;
			p[i][j] = -1;
		}
	}
	c[1][0] = 0;

	res = inf;
	for (int i = 0; i < n; i++) {
		int tmp = minCost(N - 1, i) + a[i][0];
		if (tmp < res) {
			res = tmp;
			rs[n - 1] = i;
		}
	}

	int tmp_l = rs[n - 1];
	int tmp_m = N - 1;
	int idx = n - 2;
	while (idx >= 0) {
		int tmp = p[tmp_m][tmp_l];
		if (tmp == -1) {
			break;
		}
		rs[idx] = tmp;
		tmp_m = tmp_m & ~(1 << tmp_l);
		tmp_l = tmp;
		idx--;
	}

	cout << res << endl;

	for (int i = 0; i < n; i++) {
		cout << rs[i] << ' ';
	}
	cout << endl;

	return 0;
}