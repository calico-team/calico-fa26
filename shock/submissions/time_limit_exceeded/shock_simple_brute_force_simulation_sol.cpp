#include <iostream>
using namespace std;

int grid[1000005];

void solve(){
    int n, m, q;
    cin >> n >> m >> q;

    for (int i = 0; i < n * m; i++) grid[i] = 0;

    while (q--) {
        int y, x, r;
        cin >> y >> x >> r;

        for (int i = y - r; i <= y + r; i++) {
            for (int j = x - r; j <= x + r; j++) {
                int dx = j - x, dy = i - y;
                int shock = r*r - dx*dx - dy*dy + 1;
                if (shock > 0) {
                    grid[i * m + j] = shock;
                }
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << grid[i * m + j] << ' ';
        }
        cout << '\n';
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int tcs;
    cin >> tcs;
    while (tcs--) {
        solve();
    }
    return 0;
}