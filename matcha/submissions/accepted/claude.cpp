// Bucket-collapse solution, written from the description, to cross-check ref.cpp.
#include <bits/stdc++.h>
using namespace std;
typedef unsigned int u32;
// typed interval on K bits: set = (t ? M : 0) xor [0, x]; empty if e
struct TI { bool e; int t; u32 x; };
static u32 f(u32 x, u32 y) { u32 z = x | y, c = x & y; if (c) { int h = 31 - __builtin_clz(c); z |= (2u << h) - 1; } return z; }
static TI X(TI a, TI b) { if (a.e || b.e) return {true, 0, 0}; return {false, a.t ^ b.t, f(a.x, b.x)}; }
static TI U(TI a, TI b) { if (a.e) return b; if (b.e) return a; assert(a.t == b.t);
    return {false, a.t, max(a.x, b.x)}; }
int main() {
    int T; scanf("%d", &T);
    while (T--) {
        int n; scanf("%d", &n);
        vector<u32> L(n), R(n);
        for (auto& v : L) scanf("%u", &v);
        for (auto& v : R) scanf("%u", &v);
        vector<vector<pair<u32,u32>>> bucket(30);
        u32 tot = 0;
        for (int i = 0; i < n; ++i) {
            tot ^= L[i];
            if (L[i] != R[i]) bucket[31 - __builtin_clz(L[i] ^ R[i])].push_back({L[i], R[i]});
        }
        u32 ans = 0;
        for (int K = 29; K >= 0; --K) {
            auto& bk = bucket[K];
            u32 bx = 0; for (auto& p : bk) bx ^= p.first;
            int fixedBit = ((tot ^ bx) >> K) & 1;
            if (bk.empty()) { ans |= (u32)fixedBit << K; continue; }
            ans |= 1u << K;
            int q = 1 ^ fixedBit;
            u32 M = (1u << K) - 1;
            TI G0 = {false, 0, 0}, G1 = {true, 0, 0};
            for (auto& p : bk) {
                u32 sl = p.first & M, sr = p.second & M;
                TI S = {false, 1, M ^ sl}, P = {false, 0, sr};
                TI n0 = U(X(G0, S), X(G1, P)), n1 = U(X(G1, S), X(G0, P));
                G0 = n0; G1 = n1;
            }
            TI Z = q ? G1 : G0;
            u32 lo = Z.t ? (M ^ Z.x) : 0, hi = Z.t ? M : Z.x;
            tot ^= bx ^ lo;
            if (lo != hi) bucket[31 - __builtin_clz(lo ^ hi)].push_back({lo, hi});
            bk.clear();
        }
        printf("%u\n", ans);
    }
}
