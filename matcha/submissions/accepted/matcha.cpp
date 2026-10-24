#include <bits/stdc++.h>
using namespace std;

const int LOG = 30;

int merge(int a, int b) {
	int x = (a & b);
	if (x == 0) return (a ^ b);
	int bit = 31 - __builtin_clz(x);
	return ((a ^ b) | ((1 << (bit + 1)) - 1));
}

int solve(int n, vector<pair<int, int>> lr) {
	int ans = 0;
	for (int i = LOG - 1; i >= 0; --i) {
		vector<pair<int, int>> nlr;
		vector<int> at = {0, -1};
		bool pr = true;
		for (pair<int, int>& p : lr) {
			int a = !!(p.first & (1 << i));
			int b = !!(p.second & (1 << i));
			if (a == 0 && b == 0) {
				nlr.push_back(p);
			} else if (a == 1 && b == 1) {
				nlr.push_back({p.first - (1 << i), p.second - (1 << i)});
				swap(at[0], at[1]); pr = !pr;
			} else {
				vector<int> nat = {-1, -1};
				if (at[0] != -1) {
					nat[0] = max(nat[0], merge(at[0], p.first ^ ((1 << i) - 1)));
					nat[1] = max(nat[1], merge(at[0], p.second ^ (1 << i)));
				}
				if (at[1] != -1) {
					nat[0] = max(nat[0], merge(at[1], p.second ^ (1 << i)));
					nat[1] = max(nat[1], merge(at[1], p.first ^ ((1 << i) - 1)));
				}
				pr = !pr;
				at = nat;
			}
		}
		if (at[1] != -1) {
			ans ^= 1 << i;
			if (pr) nlr.push_back({at[1] ^ ((1 << i) - 1), (1 << i) - 1});
			else nlr.push_back({0, at[1]});
		} else {
			if (pr) nlr.push_back({0, at[0]});
			else nlr.push_back({at[0] ^ ((1 << i) - 1), (1 << i) - 1});
		}
		lr = nlr;
	}
	return ans;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int t; cin >> t;
	while (t--) {
		int n; cin >> n;
		vector<pair<int, int>> lr(n);
		for (int i = 0; i < n; ++i) cin >> lr[i].first;
		for (int i = 0; i < n; ++i) cin >> lr[i].second;
		cout << solve(n, lr) << '\n';
	}
	return 0;
}
