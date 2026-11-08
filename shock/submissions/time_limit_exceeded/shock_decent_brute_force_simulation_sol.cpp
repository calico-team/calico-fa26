#include <iostream>
using namespace std;

int grid[1000005];

void solve(){
    int n, m, q;
    cin >> n >> m >> q;

    for (int i = 0; i < n * m; i++) grid[i] = 0;

    while (q--) {
        int x, y, r;
        cin >> x >> y >> r;
        x--; y--;

        int rr = r * r;
        int dx = r;
        for (int dy = 0; dy <= r; dy++) {
            while (dx * dx + dy * dy > rr) dx--;
            int base = rr + 1 - dy * dy;

            int* up = grid + (y - dy) * m + x;
            for (int k = -dx; k <= dx; k++) up[k] = base - k * k;

            if (dy) {
                int* dn = grid + (y + dy) * m + x;
                for (int k = -dx; k <= dx; k++) dn[k] = base - k * k;
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