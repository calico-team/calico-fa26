#include <bits/stdc++.h>

using namespace std;

int main() {
    int T, phase; cin >> T >> phase;
    for (int i = 0; i < T; i++) {  
        int N; cin >> N;
        if (phase == 1) {
            vector<int> P(N);
            for (int i = 0; i < N; i++) {
                cin >> P[i];
            }

            // vertex i has C[i] children
            unordered_map<int, int> C;
            for (int i = 0; i < N; i++) {
                C[P[i]]++;
            }

            // bottom 10 bits encode the parent, remaining bits encode number of children
            for (int i = 0; i < N; i++) {
                cout << P[i] + (1 << 10) * C[i + 1] << " ";
            }

            cout << endl;
        }
        else {
            vector<int> A(N);
            for (int i = 0; i < N; i++) {
                cin >> A[i];
            }

            vector<int> P(N);
            unordered_map<int, int> expC;
            int idx = -1; // index with missing value
            for (int i = 0; i < N; i++) {
                if (A[i] != -1) {
                    int parent = A[i] & ((1 << 10) - 1); // take bottom 10 bits
                    int numChildren = (A[i] ^ parent) >> 10; // take remaining bits
                    P[i] = parent;
                    expC[i + 1] = numChildren; // convert to 1 indexing, expect vertex i+1 to have numChildren children 
                }
                else {
                    expC[i + 1] = -1; // the value at this index is missing, so we don't have an expected number of children
                    idx = i;
                }
            }


            // count actual number of children for each vertex
            unordered_map<int, int> C;
            for (int i = 0; i < N; i++) {
                if (P[i] != -1) {
                    C[P[i]]++;
                }
            }

            bool fixed = false; // whether we have edited the parent array
            for (int i = 1; i < N + 1; i++) {
                // if we have an expected number but this doesn't match the actual number, this must be the parent of the missing vertex
                if (expC[i] != -1 && expC[i] != C[i]) {
                    P[idx] = i;
                    fixed = true;
                    break;
                }
            }

            // if we didn't find any mismatches, the missing vertex must be its own parent, i.e. it's the root
            if (!fixed) {
                P[idx] = idx + 1; // 1 indexing
            }

            for (int x : P) {
                cout << x << " ";
            }
            cout << endl;
        }
    }
}
