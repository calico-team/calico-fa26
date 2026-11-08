#pragma GCC optimize("O3,unroll-loops")
#include <bits/stdc++.h>
using namespace std;

static char ibuf[1 << 25];
size_t ipos = 0, ilen = 0;

inline int readInt() {
    while (ipos < ilen && (ibuf[ipos] < '0' || ibuf[ipos] > '9')) ipos++;
    int x = 0;
    while (ipos < ilen && ibuf[ipos] >= '0' && ibuf[ipos] <= '9')
        x = x * 10 + (ibuf[ipos++] - '0');
    return x;
}

struct Node { int next, val; };

int main() {
    ilen = fread(ibuf, 1, sizeof(ibuf), stdin);
    string out;
    out.reserve(1 << 23);

    int T = readInt();
    while (T--) {
        int n = readInt();
        vector<Node> g(n);
        for (int i = 0; i < n; i++) g[i].next = readInt() - 1;
        for (int i = 0; i < n; i++) g[i].val = readInt();

        // Pass 1: tail length, cycle length, cycle XOR for every node (O(N))
        vector<int> state(n, 0), tail(n), cyc(n), cx(n);
        vector<int> path;
        path.reserve(n);
        for (int s = 0; s < n; s++) {
            if (state[s]) continue;
            path.clear();
            int u = s;
            while (state[u] == 0) {
                state[u] = 1;
                path.push_back(u);
                u = g[u].next;
            }
            int k = (int)path.size();
            if (state[u] == 1) {
                // Found a new cycle starting at u
                int start = k - 1;
                while (path[start] != u) start--;
                int L = k - start, x = 0;
                for (int j = start; j < k; j++) x ^= g[path[j]].val;
                for (int j = start; j < k; j++) {
                    int v = path[j];
                    tail[v] = 0; cyc[v] = L; cx[v] = x; state[v] = 2;
                }
                k = start;
            }
            // Remaining path nodes are on the tail; fill backward
            for (int j = k - 1; j >= 0; j--) {
                int v = path[j], w = g[v].next;
                tail[v] = tail[w] + 1; cyc[v] = cyc[w]; cx[v] = cx[w];
                state[v] = 2;
            }
        }

        // Pass 2: brute-force walk from each start, only as far as needed
        const Node *gp = g.data();
        char tmp[16];
        for (int i = 0; i < n; i++) {
            int steps = tail[i] + (cx[i] == 0 ? cyc[i] : 2 * cyc[i]);
            int h = 0, best = 0, cur = i;
            for (int s = 0; s < steps; s++) {
                const Node &nd = gp[cur];
                h ^= nd.val;
                best = max(best, h);   // branchless (cmov)
                cur = nd.next;
            }
            int len = 0;
            if (best == 0) tmp[len++] = '0';
            while (best) { tmp[len++] = char('0' + best % 10); best /= 10; }
            while (len) out.push_back(tmp[--len]);
            out.push_back(i + 1 < n ? ' ' : '\n');
        }
    }
    fwrite(out.data(), 1, out.size(), stdout);
    return 0;
}