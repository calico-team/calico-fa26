#include <iostream>
using namespace std;

char grid[100005];

void solve(){
    int n, m, q;
    cin >> n >> m >> q;

    for (int i = 0; i < n * m; i++) grid[i] = '.';

    while (q--) {
        int x, y, r;
        char c;
        cin >> x >> y >> c >> r;
        x--; y--;

        for (int i = y - r; i <= y + r; i++) {
            for (int j = x - r; j <= x + r; j++) {
                int dx = j - x, dy = i - y;
                if (dx * dx + dy * dy <= r * r) {
                    grid[i * m + j] = c;
                }
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << grid[i * m + j];
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