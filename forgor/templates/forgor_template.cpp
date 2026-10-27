#include <iostream>
#include <vector>
using namespace std;

/**
 * Phase 1: encode the tree.
 *
 * N: the number of vertices
 * P: the parent array of the tree: P[i] is the parent of vertex i + 1,
 *    or i + 1 if vertex i + 1 has no parent (the root).
 * Returns: the N integers A_1..A_N, your encoding of the tree.
 */
vector<int> solve_phase1(int N, vector<int>& P) {
    // YOUR CODE HERE
    return vector<int>(N, 0);
}

/**
 * Phase 2: recover the tree from your own encoding.
 *
 * N: the number of vertices
 * A: the N integers A_1..A_N — identical to what your phase 1 output
 *    for this test case, with exactly one value replaced by -1 (the
 *    erased value).
 * Returns: the N integers P_1..P_N, the parent array of the original
 *          tree (P[i] is the parent of vertex i + 1, or i + 1 if
 *          vertex i + 1 has no parent).
 */
vector<int> solve_phase2(int N, vector<int>& A) {
    // YOUR CODE HERE
    return vector<int>(N, 0);
}

int main() {
    int T, phase;
    cin >> T >> phase;

    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;

        vector<int> A(N), P(N);
        if (phase == 1) {
            for (int j = 0; j < N; j++) {
                cin >> P[j];
            }
            A = solve_phase1(N, P);
        } else {
            for (int j = 0; j < N; j++) {
                cin >> A[j];
            }
            P = solve_phase2(N, A);
        }

        for (int j = 0; j < N; j++) {
            if (j > 0) cout << ' ';
            cout << (phase == 1 ? A[j] : P[j]);
        }
        cout << '\n';
    }
}
