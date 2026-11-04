#include <bits/stdc++.h>

using namespace std;

struct DSU {
    vector<int> parent, size;

    DSU(int n) : parent(n), size(n, 1) {
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    bool connect(int a, int b) {
        a = find(a), b = find(b);
        if (a == b) return false;
        if (size[a] < size[b]) swap(a, b);
        parent[b] = a;
        size[a] += size[b];
        return true;
    }

    bool isConnected(int a, int b) {
        return find(a) == find(b);
    }
};

vector<string> solve(int N, int M, int Q, vector<string>& G, vector<pair<int, int>>& start, vector<pair<int, int>>& end) {
    DSU dsu(N*M);
    vector<pair<int, int>> dirs = {{-1,0}, {1,0}, {0,-1}, {0,1}};
    for (int row=0; row<N; row++) {
        for (int col=0; col<M; col++) {
            for (auto [dr, dc] : dirs) {
                if (row+dr >= 0 && row+dr < N && col+dc >= 0 and col+dc < M) {
                    char cur = G[row][col];
                    char nxt = G[row+dr][col+dc];
                    if (cur == nxt || cur == '.' || nxt == '.') {
                        dsu.connect(row*M+col, (row+dr)*M+(col+dc));
                    }
                }
            }
        }
    }

    vector<string> ans;
    for (int i=0; i<Q; i++) {
        auto [start_row, start_col] = start[i];
        auto [end_row, end_col] = end[i];
        ans.push_back(dsu.isConnected(start_row*M+start_col, end_row*M+end_col) ? "YES" : "NO");
    }
    return ans;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, M, Q;
        cin >> N >> M >> Q;
        vector<string> G(N);
        for (int j = 0; j < N; j++) {
            cin >> G[j];
        }
        vector<pair<int, int>> start, end;
        for (int j = 0; j < Q; j++) {
            int start_row, start_col, end_row, end_col;
            cin >> start_row >> start_col >> end_row >> end_col;
            start.push_back({start_row, start_col});
            end.push_back({end_row, end_col});
        }

        for (string s : solve(N, M, Q, G, start, end)) {
            cout << s << '\n';
        }
    }
}
