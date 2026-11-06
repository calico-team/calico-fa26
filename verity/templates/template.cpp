#include <bits/stdc++.h>
using namespace std;

void solve(int N, int K, vector<char>& A) {
    // YOUR CODE HERE
}

int main() {
    cout << unitbuf;
    int T;
    cin >> T;
    
    for (int i = 0; i < T; i++) {
        int N, K;
        cin >> N >> K;

        vector<char> A(K);
        for (int j = 0; j < K; j++) {
            cin >> A[j];
        }

        solve(N, K, A);
    }

    return 0;
}
