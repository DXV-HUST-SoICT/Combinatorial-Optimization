#include <bits/stdc++.h>

using namespace std;

const int NMAX = 10000;

int n, m;
vector<int> a[NMAX];
vector<int> b[NMAX];
vector<int> l[NMAX];
vector<int> k[NMAX];
int dist[NMAX];
int inf = 0;

void _init() {
	dist[0] = 0;
	for (int i = 1; i < n; i++) {
		dist[i] = inf;
	}
}

int iterative_dp() {
	_init();
	for (int i = 1; i < n; i++) {
		for (int j = 0; j < b[i].size(); j++) {
			dist[i] = min(dist[i], dist[b[i][j]] + k[i][j]);
		}
	}
	return dist[n - 1];
}

void _try(int i) {
	if (dist[i] < inf) {
		return;
	}
	for (int j = 0; j < b[i].size(); j++) {
		_try(b[i][j]);
		dist[i] = min(dist[i], dist[b[i][j]] + k[i][j]);
	}
}

int recursive_dp() {
	_init();
	_try(n - 1);
	return dist[n - 1];
}

int bf_fwd_prop() {
	_init();
	for (int i = 0; i < n; i++) {
		if (dist[i] == inf) {
			continue;
		}
		for (int j = 0; j < a[i].size(); j++) {
			dist[a[i][j]] = min(dist[a[i][j]], dist[i] + l[i][j]);
		}
	}
	return dist[n - 1];
}

void _fwd(int i) {
	for (int j = 0; j < a[i].size(); j++) {
		if (dist[a[i][j]] > dist[i] + l[i][j]) {
			dist[a[i][j]] = dist[i] + l[i][j];
			_fwd(a[i][j]);
		}
	}
}

int df_fwd_prop() {
	_init();
	_fwd(0);
	return dist[n - 1];
}

int main() {
	freopen("dag.txt", "r", stdin);
	cin >> n >> m;
	int u, v, d;
	for (int i = 0; i < m; i++) {
		cin >> u >> v >> d;
		a[u].push_back(v);
		l[u].push_back(d);
		b[v].push_back(u);
		k[v].push_back(d);
		inf += d;
	}
	inf *= 2;

	int (*solver[])() = {
		&iterative_dp,
		&recursive_dp,
		&bf_fwd_prop,
		&df_fwd_prop
	};
	int nf = sizeof(solver) / sizeof(solver[0]);

	for (int i = 0; i < nf; i++) {
		cout << solver[i]() << endl;
	}

	return 0;
}