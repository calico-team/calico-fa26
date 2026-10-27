#include <iostream>
#include <vector>
#include <string>
using namespace std;

/**
 * Return the total units of rain collected over the K nights.
 *
 * N: the number of drones
 * X: the starting x coordinate of each drone
 * Y: the starting y coordinate of each drone
 * Z: the starting z coordinate of each drone
 * DIR: the direction of each drone, one of 'N' or 'E'
 * K: the number of nights
 */
long long solve(int N, vector<int>& X, vector<int>& Y, vector<int>& Z, vector<string>& DIR, long long K) {
    // YOUR CODE HERE
    return -1;
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int N;
        long long K;
        cin >> N >> K;
        vector<int> X(N), Y(N), Z(N);
        vector<string> DIR(N);
        for (int j = 0; j < N; j++) {
            cin >> X[j] >> Y[j] >> Z[j] >> DIR[j];
        }
        cout << solve(N, X, Y, Z, DIR, K) << '\n';
    }
}
