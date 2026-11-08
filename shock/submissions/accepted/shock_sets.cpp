#include <iostream>
#include <vector>
#include <set>
using namespace std;

void solve() {
    int n, m, q;
    cin >> n >> m >> q;
    bool swapDimensions = (m > n);   // make rows short: m <= n
    if (swapDimensions) swap(n, m);
    
    vector<int> xs(q), ys(q), rs(q);
    for (int i = 0; i < q; i++) {
        int y, x, r;
        cin >> y >> x >> r;
        x--; y--;
        if (swapDimensions) swap(x, y);
        xs[i] = x; ys[i] = y; rs[i] = r;
    }

    vector<set<int>> freeCols(n);
    for (int y = 0; y < n; y++) {
        // auto hint = freeCols[y].end();
        // for (int x = 0; x < m; x++) hint = freeCols[y].insert(hint, x);
        for (int x = 0; x < m; x++) {
            freeCols[y].insert(x);
        }
    }

    vector<vector<int>> answer(n, vector<int>(m, 0));

    for (int i = q - 1; i >= 0; i--) {
        int x = xs[i], y = ys[i], r = rs[i];
        long long rr = 1LL * r * r;
        int dx = r;
        for (int dy = 0; dy <= r; dy++) {
            while (1LL * dx * dx + 1LL * dy * dy > rr) dx--;
            int lo = x - dx, hi = x + dx;
            for (int row : {y - dy, y + dy}) {
                auto& s = freeCols[row];
                auto it = s.lower_bound(lo);
                while (it != s.end() && *it <= hi) {
                    answer[row][*it] = r*r - ((row-y)*(row-y)+(*it-x)*(*it-x)) + 1;
                    it = s.erase(it);
                }
                if (dy == 0) break;   // center row only once
            }
        }
    }

    if(swapDimensions){
        for(int x = 0; x < m; x++){
            for(int y = 0; y < n; y++){
                cout<<answer[y][x]<<' ';
            }
            cout<<'\n';
        }
    }
    else{
        for(int y = 0; y < n; y++){
            for(int x = 0; x < m; x++){
                cout<<answer[y][x]<<' ';
            }
            cout<<'\n';
        }
    }
}

int main() {
    int tcs;
    cin >> tcs;
    while (tcs--) solve();
}