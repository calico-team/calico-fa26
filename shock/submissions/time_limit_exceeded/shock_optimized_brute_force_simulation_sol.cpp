#pragma GCC optimize("O3,unroll-loops,omit-frame-pointer,inline")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#include <cstdio>
#include <cstring>

static char inbuf[1 << 23];
static int grid[1000005];
static char outbuf[1 << 21];
static const char* ip;

static inline int readInt() {
    while (*ip <= ' ') ip++;
    int v = 0;
    while (*ip > ' ') v = v * 10 + (*ip++ - '0');
    return v;
}

int main() {
    size_t len = fread(inbuf, 1, sizeof(inbuf) - 1, stdin);
    inbuf[len] = 0;
    ip = inbuf;

    int tcs = readInt();
    size_t op = 0;
    const size_t CAP = sizeof(outbuf);

    while (tcs--) {
        int n = readInt(), m = readInt(), q = readInt();
        memset(grid, 0, sizeof(int) * (size_t)n * m); // zeroing is still fine

        while (q--) {
            int y = readInt() - 1;
            int x = readInt() - 1;
            int r = readInt();
            int rr = r * r;

            int dx = r;
            for (int dy = 0; dy <= r; dy++) {
                while (dx * dx + dy * dy > rr) dx--;
                int base = rr + 1 - dy * dy;

                int* up = grid + (size_t)(y - dy) * m + x;
                for (int k = -dx; k <= dx; k++) up[k] = base - k * k;

                if (dy) {
                    int* dn = grid + (size_t)(y + dy) * m + x;
                    for (int k = -dx; k <= dx; k++) dn[k] = base - k * k;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            // worst case ~12 bytes per cell (value + separator) + newline
            if (op + (size_t)m * 12 + 2 > CAP) {
                fwrite(outbuf, 1, op, stdout);
                op = 0;
            }
            const int* row = grid + (size_t)i * m;
            for (int j = 0; j < m; j++) {
                unsigned v = (unsigned)row[j];
                if (v < 10) {
                    outbuf[op++] = '0' + v;
                } else {
                    char tmp[12];
                    int t = 0;
                    while (v) { tmp[t++] = '0' + v % 10; v /= 10; }
                    while (t) outbuf[op++] = tmp[--t];
                }
                outbuf[op++] = (j + 1 < m) ? ' ' : '\n';
            }
        }
    }
    fwrite(outbuf, 1, op, stdout);
    return 0;
}