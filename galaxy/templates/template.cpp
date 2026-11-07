#include <bits/stdc++.h>
using namespace std;

/*
* Output YES or NO for all the queries
* N: Number of rows
* M: Number of columns
* Q: Number of queries
* start: vector pair of the starting coordinates for each query
* end: vector pair of the ending coordinates for each query
*/

vector<string> solve(int N, int M, int Q, vector<string>& G, vector<pair<int, int>>& start, vector<pair<int, int>>& end) {
    vector<string> ans;
    return ans;
}
int main(){
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