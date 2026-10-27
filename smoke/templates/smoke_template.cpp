#include <iostream>
#include <vector>
using namespace std;

/**
 * Return whether Omen can throw a smoke for every teammate request.
 *
 * N: the number of requests
 * R: the number of seconds it takes for a smoke to recharge
 * A: the times (in seconds) at which each request is made
 */
string solve(int N, int R, vector<int>& A) {
    // YOUR CODE HERE
    return "";
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int N, R;
        cin >> N >> R;
        vector<int> A(N);
        for (int j = 0; j < N; j++) {
            cin >> A[j];
        }
        cout << solve(N, R, A) << '\n';
    }
}
