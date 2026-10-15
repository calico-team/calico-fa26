#include <bits/stdc++.h>

using namespace std;

string solve(int N, int M, vector<string>& G) {
    stack<pair<int, int>> s({{0,0}});
    vector<vector<bool>> visited(N, vector<bool>(M));
    vector<pair<int, int>> dirs = {{-1,-1}, {-1,1}, {1,-1}, {1,1}};
    while (!s.empty()) {
        auto [row, col] = s.top();
        s.pop();
        if (row == N-1 and col == M-1) {
            return "YES";
        }
        visited[row][col] = true;
        for (auto [dr, dc] : dirs) {
            if (row+dr >= 0 && row+dr < N && col+dc >= 0 and col+dc < M) {
                char cur = G[row][col];
                char nxt = G[row+dr][col+dc];
                if (!visited[row+dr][col+dc] && (cur == nxt || cur == '.' || nxt == '.')) {
                    s.push({row+dr, col+dc});
                }
            }
        }
        return "NO";
    }
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, M;
        cin >> N >> M;
        vector<string> G(N);
        for (int j = 0; j < N; j++) {
            cin >> G[j];
        }
        cout << solve(N, M, G) << '\n';
    }
}
