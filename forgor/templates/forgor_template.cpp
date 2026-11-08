#include <iostream>
#include <vector>
#include <string>
using namespace std;

/**
 * Phase 1: encode the tree.
 *
 * N: the number of vertices
 * E: the N - 1 edges of the tree as (u, v) pairs, in arbitrary
 *    order — not necessarily lexicographically increasing, and u is
 *    not guaranteed to be the parent of v
 * Returns: the N integers A_1..A_N, your encoding of the tree
 */
vector<int> solve_phase1(int N, vector<pair<int, int>>& E) {
    // YOUR CODE HERE
    return vector<int>(N, 0);
}

/**
 * Phase 2: recover the tree from your own encoding.
 *
 * N: the number of vertices
 * A: the N integers A_1..A_N — identical to what your phase 1 output
 *    for this test case, with exactly one value replaced by -1 (the
 *    erased value)
 * Returns: the N - 1 edges of the original tree as (u, v) pairs, one
 *          edge per output line (the checker compares the set of
 *          edges, so the order and orientation of the pairs do not
 *          matter)
 */
vector<pair<int, int>> solve_phase2(int N, vector<int>& A) {
    // YOUR CODE HERE
    return {};
}

int main() {
    string phase;
    cin >> phase;
    int N;
    cin >> N;

    if (phase == "FIRST") {
        vector<pair<int, int>> E(N - 1);
        for (int i = 0; i < N - 1; i++) {
            cin >> E[i].first >> E[i].second;
        }
        vector<int> A = solve_phase1(N, E);
        for (int i = 0; i < N; i++) {
            if (i > 0) cout << ' ';
            cout << A[i];
        }
        cout << '\n';
    } else {
        vector<int> A(N);
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }
        vector<pair<int, int>> edges = solve_phase2(N, A);
        for (auto& e : edges) {
            cout << e.first << ' ' << e.second << '\n';
        }
    }
}
