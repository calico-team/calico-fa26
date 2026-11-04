#include <iostream>
#include <vector>
using namespace std;

const int N = 2e5, LOG = 30;

int cnt[3 * LOG * N + 1], ch[3 * LOG * N + 1][2], ans[N];
vector<int> into[N];
bool vis[N];
int nxt = 1, xr = 0;

int nw() {
	cnt[nxt] = ch[nxt][0] = ch[nxt][1] = 0;
	return nxt++;
}

int mk(int& x) {
	if (x != 0) return x;
	return x = nw();
}

void chv(int cur, int x, int v) {
	x ^= xr;
	cnt[cur] += v;
	for (int b = 29; b >= 0; --b) {
		if (x & (1 << b)) cur = mk(ch[cur][1]);
		else cur = mk(ch[cur][0]);
		cnt[cur] += v;
	}
}

int gt(int cur) {
	int ans = 0;
	for (int b = 29; b >= 0; --b) {
		int h = !!(xr & (1 << b));
		if (cnt[ch[cur][h ^ 1]] > 0) {
			ans ^= 1 << b; cur = ch[cur][h ^ 1];
		} else cur = ch[cur][h];
	}
	return ans;
}

void trav(int cur, int node, vector<int>& V, bool f = false) {
	if (!f) { xr ^= V[node]; chv(cur, 0, 1); }
	vis[node] = true; ans[node] = gt(cur);
	for (int i : into[node]) if (!vis[i]) trav(cur, i, V);
	if (!f) { chv(cur, 0, -1); xr ^= V[node]; }
}

/**
 * Return an array of N integers, the i-th of which
 * represents Big Ben's maximum happiness if he
 * starts by trying to define word i.
 *
 * N: the number of words in the dictionary
 * A: the first word in the definition of word i
 * V: the value associated with the happiness of each word
 */
vector<int> solve(int n, vector<int> A, vector<int> V) {
	nxt = 1;
	for (int& i : A) --i;
	for (int i = 0; i < n; ++i) {
		vis[i] = false;
		into[A[i]].push_back(i);
	}
	for (int i = 0; i < n; ++i) {
		if (vis[i]) continue;
		int root = nw(); xr = 0; chv(root, 0, 1);
		int a = i, b = A[i];
		while (a != b) { a = A[a]; b = A[A[b]]; }
		vector<int> cyc = {a};
		while (A[cyc.back()] != cyc.front()) cyc.push_back(A[cyc.back()]);
		for (int j : cyc) vis[j] = true;
		for (int k = 0; k < 2; ++k) for (int j = (int) cyc.size() - 1; j >= 0; --j) { xr ^= V[cyc[j]]; chv(root, 0, 1); }
		for (int j = (int) cyc.size() - 1; j >= 0; --j) {
			xr ^= V[cyc[j]]; chv(root, 0, 1);
			trav(root, cyc[j], V, true);
		}
	}
	for (int i = 0; i < n; ++i) into[i].clear();
	vector<int> ret(n);
	for (int i = 0; i < n; ++i) ret[i] = ans[i];
	return ret;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int T; cin >> T;
	while (T--) {
		int N; cin >> N;
		vector<int> A(N), V(N);
		for (int& i : A) cin >> i;
		for (int& i : V) cin >> i;
		vector<int> ans = solve(N, A, V);
		for (int& i : ans) cout << i << ' ';
		cout << '\n';
	}
	return 0;
}

