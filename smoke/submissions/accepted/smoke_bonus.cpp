#include <iostream>
#include <vector>

using namespace std;

string solve() {
    int n, r;
    cin >> n >> r;
    vector<int> times(n + 1);
    times[0] = 0;

    for(int i = 0; i < n; ++i){
        cin >> times[i + 1];
    }
    
    int wait = 2 * r;
    
    for(int i = 1; i <= n; ++i){
        wait += times[i] - times[i - 1];
        wait = min(2 * r, wait);
        
        if (wait >= r){
            wait -= r;
        } else{
            return "NO";
        }
    }

    return "YES";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cout << solve() << '\n';
    }
}