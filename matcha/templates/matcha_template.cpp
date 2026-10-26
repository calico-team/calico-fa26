#include <iostream>
#include <vector>
using namespace std;

int solve(int n, vector<int> l, vector<int> r) {
	return 0;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int t; cin >> t;
	while (t--) {
		int n; cin >> n;
		vector<int> l(n), r(n);
		for (int& i : l) cin >> i;
		for (int& i : r) cin >> i;
		cout << solve(n, l, r) << '\n';
	}
	return 0;
}
