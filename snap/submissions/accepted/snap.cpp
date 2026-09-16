#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

const bool HAS_TC = 1;

void solve() {
	int m, n, f; cin >> m >> n >> f;
	vector<string> grid(m);
	for (string& i : grid) cin >> i;
	vector<int> lox(10, 1000), loy(10, 1000), hix(10, -1), hiy(10, -1);
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			if (grid[i][j] == '.') continue;
			int v = grid[i][j] - '0';
			lox[v] = min(lox[v], i); loy[v] = min(loy[v], j);
			hix[v] = max(hix[v], i); hiy[v] = max(hiy[v], j);
		}
	}
	for (int i = 0; i < 10; ++i) {
		if (lox[i] == 1000) continue;
		if (hix[i] - lox[i] + 1 <= f && hiy[i] - loy[i] + 1 <= f) {
			lox[i] = min(lox[i], m - f);
			loy[i] = min(loy[i], n - f);
			for (int a = lox[i]; a < lox[i] + f; ++a) {
				for (int b = loy[i]; b < loy[i] + f; ++b) {
					cout << grid[a][b];
				}
				cout << '\n';
			}
			return;
		}
	}
	cout << "IMPOSSIBLE\n";
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int t = 1; if (HAS_TC) cin >> t;
	while (t--) solve();
	return 0;
}

