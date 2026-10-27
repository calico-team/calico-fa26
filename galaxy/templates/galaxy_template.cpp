#include <iostream>
#include <vector>
#include <string>
using namespace std;

/**
 * Return whether Ben can reach the bottom-right tile of the grid.
 *
 * N: the number of rows in the grid
 * M: the number of columns in the grid
 * G: the grid, where G[i] is the i-th row and each character is one of
 *    'R', 'B', or '.'
 */
string solve(int N, int M, vector<string>& G) {
    // YOUR CODE HERE
    return "";
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int N, M;
        cin >> N >> M;
        vector<string> G(N);
        for (int j = 0; j < N; j++) {
            cin >> G[j];
        }
        cout << solve(N, M, G) << '\n';
    }
}
