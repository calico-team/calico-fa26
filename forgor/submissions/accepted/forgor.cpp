#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    string phase; cin >> phase;
    int N; cin >> N;
    if (phase == "FIRST") {
        // convert edge representation to parent list representation
        vector<int> P(N + 1, -1);
        vector<int> C(N + 2, 0);
        for (int i = 0; i < N - 1; i++) {
            int p, c; cin >> p >> c;

            P[c] = p;
            C[p]++;
        }

        // bottom bit encodes parity of number of children, remaining bits encode parent
        for (int i = 1; i < N + 1; i++) {
            if (P[i] == -1) {
                P[i] = i; // if root, store own index as parent
            }
            cout << (C[i] % 2) + 2 * P[i] << " ";
        }
        cout << endl;
    }
    else {
        vector<int> A(N + 1);
        for (int i = 1; i < N + 1; i++) {
            cin >> A[i];
        }

        vector<int> P(N + 1, -1);
        vector<int> expParity(N + 2, -1);
        int idx = -1; // index with missing value
        for (int i = 1; i < N + 1; i++) {
            if (A[i] != -1) {
                int childrenParity = (int)(A[i] & 1); // take bottom bit
                int parent = (int)(A[i] >> 1); // take remaining bits
                P[i] = parent;
                expParity[i] = childrenParity; // convert to 1 indexing, expect vertex i+1 to have numChildren children 
            }
            else {
                idx = i;
            }
        }


        // count actual number of children for each vertex
        vector<int> C(N + 2, 0);
        for (int i = 1; i < N + 1; i++) {
            if (P[i] != -1) {
                C[P[i]]++;
            }
        }

        bool fixed = false; // whether we have edited the parent array
        for (int i = 1; i < N + 1; i++) {
            // if we have an expected parity but this doesn't match the parity of the actual number, this must be the parent of the missing vertex
            if (expParity[i] != -1 && expParity[i] != (C[i] % 2)) {
                P[idx] = i;
                fixed = true;
                break;
            }
        }

        // if we didn't find any mismatches, the missing vertex must be its own parent, i.e. it's the root
        if (!fixed) {
            P[idx] = idx;
        }

        vector<pair<int, int>> edges;
        for (int i = 1; i < N + 1; i++) {
            if (P[i] != i) {
                edges.push_back(make_pair(P[i], i));
            }
        }

        sort(edges.begin(), edges.end());

        for (auto& e : edges) {
            cout << e.first << " " << e.second << "\n";
        }
    }
}
