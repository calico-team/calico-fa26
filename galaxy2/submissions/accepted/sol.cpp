#include <bits/stdc++.h>

using namespace std;

vector<string> solve(int N, int M, int Q, vector<string>& G, vector<pair<int, int>>& start, vector<pair<int, int>>& end, vector<int>& K) {
    const int INF = INT_MAX / 2;
    vector<int> dist(N * M * 2, INF), ans(Q, INF);
    int dr[4] = {-1, 1, 0, 0}, dc[4] = {0, 0, -1, 1};

    auto id = [&](int r, int c, int s) { return (r * M + c) * 2 + s; };
    auto valid = [&](int r, int c, int s) { return G[r][c] == '.' || G[r][c] == "RB"[s]; };

    auto bfs = [&](int r0, int r1, int c0, int c1, int sr, int sc, int ss) {
        for (int r = r0; r <= r1; r++) {
            for (int c = c0; c <= c1; c++) {
                dist[id(r, c, 0)] = dist[id(r, c, 1)] = INF;
            }
        }
        queue<array<int, 3>> bfs_queue;
        dist[id(sr, sc, ss)] = 0;
        bfs_queue.push({sr, sc, ss});
        while (!bfs_queue.empty()) {
            auto [r, c, s] = bfs_queue.front();
            bfs_queue.pop();
            int d = dist[id(r, c, s)];
            if (G[r][c] == '.' && dist[id(r, c, 1 - s)] == INF) {
                dist[id(r, c, 1 - s)] = d + 1;
                bfs_queue.push({r, c, 1 - s});
            }
            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k], nc = c + dc[k];
                if (nr >= r0 && nr <= r1 && nc >= c0 && nc <= c1 && valid(nr, nc, s) && dist[id(nr, nc, s)] == INF) {
                    dist[id(nr, nc, s)] = d + 1;
                    bfs_queue.push({nr, nc, s});
                }
            }
        }
    };

    function<void(int, int, int, int, vector<int>&)> divide = [&](int r0, int r1, int c0, int c1, vector<int>& qs) {
        if (r0 > r1 || c0 > c1 || qs.empty()) {
            return;
        }
        bool split_col = c1 - c0 >= r1 - r0;
        int mid = split_col ? (c0 + c1) / 2 : (r0 + r1) / 2;
        vector<pair<int, int>> sep;
        if (split_col) {
            for (int r = r0; r <= r1; r++) sep.push_back({r, mid});
        } else {
            for (int c = c0; c <= c1; c++) sep.push_back({mid, c});
        }

        map<int, vector<int>> queries_from;
        for (int q : qs) {
            queries_from[id(start[q].first, start[q].second, 1)].push_back(q);
        }

        for (auto [r, c] : sep) {
            for (int s = 0; s < 2; s++) {
                if (!valid(r, c, s)) continue;
                bfs(r0, r1, c0, c1, r, c, s);
                for (auto& [u, group] : queries_from) {
                    if (dist[u] == INF) continue;
                    for (int q : group) {
                        auto [er, ec] = end[q];
                        ans[q] = min(ans[q], dist[u] + min(dist[id(er, ec, 0)], dist[id(er, ec, 1)]));
                    }
                }
            }
        }

        vector<int> first, second;
        for (int q : qs) {
            int a = split_col ? start[q].second : start[q].first;
            int b = split_col ? end[q].second : end[q].first;
            if (a < mid && b < mid) first.push_back(q);
            if (a > mid && b > mid) second.push_back(q);
        }
        if (split_col) {
            divide(r0, r1, c0, mid - 1, first);
            divide(r0, r1, mid + 1, c1, second);
        } else {
            divide(r0, mid - 1, c0, c1, first);
            divide(mid + 1, r1, c0, c1, second);
        }
    };

    vector<int> qs(Q);
    iota(qs.begin(), qs.end(), 0);
    divide(0, N - 1, 0, M - 1, qs);

    vector<string> res;
    for (int q = 0; q < Q; q++) {
        res.push_back(ans[q] <= K[q] ? "YES" : "NO");
    }
    return res;
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
        vector<int> K;
        for (int j = 0; j < Q; j++) {
            int start_row, start_col, end_row, end_col, k;
            cin >> start_row >> start_col >> end_row >> end_col >> k;
            start.push_back({start_row, start_col});
            end.push_back({end_row, end_col});
            K.push_back(k);
        }

        for (string s : solve(N, M, Q, G, start, end, K)) {
            cout << s << '\n';
        }
    }
}
