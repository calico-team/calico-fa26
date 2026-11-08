#include <bits/stdc++.h>

using namespace std;

vector<string> solve(int N, int M, int Q, vector<string>& G, vector<pair<int, int>>& start, vector<pair<int, int>>& end) {
    queue<pair<int, int>> q({{N-1, M-1}});
    vector<vector<bool>> visited(N, vector<bool>(M));
    visited[N-1][M-1] = true;
    vector<pair<int, int>> dirs = {{-1,0}, {1,0}, {0,-1}, {0,1}};
    while (!q.empty()) {
        auto [row, col] = q.front();
        q.pop();
        for (auto [dr, dc] : dirs) {
            if (row+dr >= 0 && row+dr < N && col+dc >= 0 and col+dc < M) {
                char cur = G[row][col];
                char nxt = G[row+dr][col+dc];
                if (!visited[row+dr][col+dc] && (cur == nxt || cur == '.' || nxt == '.')) {
                    visited[row+dr][col+dc] = true;
                    q.push({row+dr, col+dc});
                }
            }
        }
    }
    
    vector<string> ans;
    for (auto [start_row, start_col] : start) {
        ans.push_back(visited[start_row][start_col] ? "YES" : "NO");
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
