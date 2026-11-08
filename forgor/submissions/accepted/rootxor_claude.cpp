#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string phase;
    cin >> phase;
    int n;
    cin >> n;

    if (phase == "FIRST") {
        vector<vector<int>> adj(n + 1);
        for (int i = 0; i < n - 1; i++) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        // BFS from root = 1 to find parents
        vector<int> par(n + 1, 0);
        vector<bool> vis(n + 1, false);
        queue<int> q;
        q.push(1);
        vis[1] = true;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : adj[u]) {
                if (!vis[v]) {
                    vis[v] = true;
                    par[v] = u;
                    q.push(v);
                }
            }
        }

        vector<int> A(n + 1);
        int x = 0;
        for (int i = 2; i <= n; i++) {
            A[i] = par[i];
            x ^= A[i];
        }
        A[1] = n + x;  // x < 2^18, so A[1] < 2e5 + 262144 < 1e6

        string out;
        out.reserve(n * 8);
        for (int i = 1; i <= n; i++) {
            out += to_string(A[i]);
            out += (i == n ? '\n' : ' ');
        }
        cout << out;
    } else {
        vector<int> A(n + 1);
        int missing = -1;
        for (int i = 1; i <= n; i++) {
            cin >> A[i];
            if (A[i] == -1) missing = i;
        }

        // If a non-root value was erased, recover it from the root's XOR
        if (missing != 1) {
            int x = A[1] - n;  // XOR of A[2..n]
            for (int i = 2; i <= n; i++) {
                if (i != missing) x ^= A[i];
            }
            A[missing] = x;
        }
        // If the root value was erased, we don't need it: all parents are intact

        string out;
        out.reserve(n * 14);
        for (int i = 2; i <= n; i++) {
            out += to_string(i);
            out += ' ';
            out += to_string(A[i]);
            out += '\n';
        }
        cout << out;
    }
    return 0;
}
