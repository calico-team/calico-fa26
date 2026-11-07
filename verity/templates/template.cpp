#include <bits/stdc++.h>
using namespace std;

/*
* Print a string that could be the answer string
*
* N: Length of the string
* K: Number of different -ities
* A: List containing the different -ities
*/

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
