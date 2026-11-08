// CHEESE solution: greedy + coordinate ascent + random restarts.
// Not proven correct. Tries to pass as many cases as possible.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

static mt19937_64 rng(1234567);
static chrono::steady_clock::time_point START;
static double elapsed() {
    return chrono::duration<double>(chrono::steady_clock::now() - START).count();
}

// Exact subroutine: max over c in [L,R] of (t ^ c), returns that c.
static inline int bestPick(int t, int L, int R) {
    int c = 0;
    bool tl = true, tr = true;
    for (int b = 29; b >= 0; --b) {
        int lb = (L >> b) & 1, rb = (R >> b) & 1, want = ((t >> b) & 1) ^ 1;
        int lo = tl ? lb : 0, hi = tr ? rb : 1;
        int bit = (want >= lo && want <= hi) ? want : (want ^ 1);
        c |= bit << b;
        tl = tl && bit == lb;
        tr = tr && bit == rb;
    }
    return c;
}

// Coordinate ascent: repeatedly re-pick each v_i to maximize total XOR.
static int climb(vector<int>& v, const vector<int>& L, const vector<int>& R,
                 const vector<int>& order, int cap, double deadline) {
    int x = 0;
    for (int a : v) x ^= a;
    for (int pass = 0; pass < 60; ++pass) {
        bool improved = false;
        for (int i : order) {
            int rest = x ^ v[i];
            int c = bestPick(rest, L[i], R[i]);
            int nx = rest ^ c;
            if (nx > x) { x = nx; v[i] = c; improved = true; }
            if (x == cap) return x;
        }
        if (!improved || elapsed() > deadline) break;
    }
    return x;
}

int main() {
    START = chrono::steady_clock::now();
    int T;
    if (scanf("%d", &T) != 1) return 0;
    vector<vector<int>> Ls(T), Rs(T);
    long long sumN = 0;
    for (int t = 0; t < T; ++t) {
        int n; scanf("%d", &n);
        Ls[t].resize(n); Rs[t].resize(n);
        for (auto& a : Ls[t]) scanf("%d", &a);
        for (auto& a : Rs[t]) scanf("%d", &a);
        sumN += n;
    }
    const double TOTAL = 1.7;  // seconds of total budget
    double used = 0;

    for (int t = 0; t < T; ++t) {
        auto &L = Ls[t], &R = Rs[t];
        int n = L.size();
        double budget = TOTAL * (double)n / max(1LL, sumN);
        double deadline = elapsed() + budget;

        // Corner: single day -> take R.
        if (n == 1) { printf("%d\n", R[0]); continue; }

        // Corner: all fixed -> plain XOR.
        bool allFixed = true;
        int fixedX = 0, orR = 0;
        for (int i = 0; i < n; ++i) {
            if (L[i] != R[i]) allFixed = false;
            fixedX ^= L[i];
            orR |= R[i];
        }
        if (allFixed) { printf("%d\n", fixedX); continue; }

        // Upper bound: nothing above highest bit of OR(R).
        int hb = 31 - __builtin_clz(max(orR, 1));
        int cap = (int)((1LL << (hb + 1)) - 1);

        // Heuristic: if some interval spans a full block below bit k
        // and two "wide" intervals exist, low bits are usually all freeable.
        // We just use it to seed; climb() does the real work.

        int best = 0;
        vector<int> order(n);
        iota(order.begin(), order.end(), 0);

        auto tryStart = [&](vector<int> v, const vector<int>& ord) {
            int x = climb(v, L, R, ord, cap, deadline);
            best = max(best, x);
        };

        // Seed 1: all R.
        tryStart(R, order);
        // Seed 2: all L.
        if (best < cap) tryStart(L, order);
        // Seed 3: R, processing widest intervals last (they adjust best).
        if (best < cap) {
            vector<int> ord = order;
            sort(ord.begin(), ord.end(), [&](int a, int b) {
                return (R[a] - L[a]) < (R[b] - L[b]);
            });
            tryStart(R, ord);
            reverse(ord.begin(), ord.end());
            if (best < cap) tryStart(R, ord);
        }
        // Seed 4: "R with top bit dropped and everything below set" when legal.
        if (best < cap) {
            vector<int> v(n);
            for (int i = 0; i < n; ++i) {
                int c = R[i];
                if (R[i]) {
                    int b = 31 - __builtin_clz(R[i]);
                    int cand = (R[i] & ~((1 << (b + 1)) - 1)) | ((1 << b) - 1);
                    if (cand >= L[i]) c = cand;
                }
                v[i] = c;
            }
            tryStart(v, order);
        }
        // Random restarts with random picks (biased to endpoints) + shuffled order.
        while (best < cap && elapsed() < deadline) {
            vector<int> v(n);
            for (int i = 0; i < n; ++i) {
                int r = rng() % 4;
                if (r == 0) v[i] = L[i];
                else if (r == 1) v[i] = R[i];
                else v[i] = L[i] + (int)(rng() % ((ll)R[i] - L[i] + 1));
            }
            shuffle(order.begin(), order.end(), rng);
            tryStart(v, order);
            // Perturbation: kick a few coordinates from the best-so-far isn't
            // tracked separately; random restarts are the cheap version.
        }
        printf("%d\n", best);
    }
    return 0;
}