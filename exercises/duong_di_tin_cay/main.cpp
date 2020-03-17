#include <bits/stdc++.h>

using namespace std;

const int NMAX = 1000;
const int HMAX = 20000;

vector<pair<int, double>> l[NMAX];
double dist1[NMAX][HMAX + 1], dist2[NMAX][HMAX + 1];
bool flag1[NMAX][HMAX + 1], flag2[NMAX][HMAX + 1];
double inf = 0;
int n, m;

void _try(double dist[NMAX][HMAX + 1], bool flag[NMAX][HMAX + 1], int v, int k) {
	if (!flag[v][k]) {
		for (int i = 0; i < l[v].size(); i++) {
			int u = l[v][i].first;
			_try(dist, flag, u, k - 1);
			dist[v][k] = min(dist[v][k], dist[u][k - 1] + l[v][i].second);
		}
		flag[v][k] = true;
	}
}

double algo1(int s, int t, int h) {
	memset(flag1, false, sizeof(flag1));

	for (int i = 0; i < n; i++) {
		dist1[i][0] = inf;
		flag1[i][0] = true;

		for (int j = 1; j <= h; j++) {
			dist1[i][j] = inf;
		}
	}

	for (int i = 0; i <= h; i++) {
		dist1[s][i] = 0;
		flag1[s][i] = true;
	}

	_try(dist1, flag1, t, h);

	return dist1[t][h];
}

double algo2(int s, int t, int h) {
	memset(flag2, false, sizeof(flag2));

	for (int i = 0; i < n; i++) {
		dist2[i][0] = inf;
		flag2[i][0] = true;

		for (int j = 1; j <= h; j++) {
			dist2[i][j] = inf;
		}
	}

	dist2[s][0] = 0;

	_try(dist2, flag2, t, 0);
	double res = dist2[t][0];

	for (int i = 1; i <= h; i++) {
		_try(dist2, flag2, t, i);
		res = min(res, dist2[t][i]);
	}

	return res;
}

int main() {
	freopen("1000EWD.txt", "r", stdin);
	freopen("result1.csv", "w", stdout);

	cin >> n;
	cin >> m;

	int u, v;
	double d;

	for (int i = 0; i < m; i++) {
		cin >> u >> v >> d;
		inf += d;
		l[u].push_back(make_pair(v, d));
	}

	inf *= 10;

	cout << "id,s,t,h,r1,r2\n";

	int s, t, h;

	for (int id = 0; id < 100; id++) {
		cout << id << ',';
		s = rand() % n;
		t = rand() % n;
		h = rand() % (HMAX + 1);
		cout << s << ',' << t << ',' << h << ',' << algo1(s, t, h) << ',' << algo2(s, t, h) << endl;
	}

	return 0;
}