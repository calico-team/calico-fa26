#pragma GCC optimize("O3,unroll-loops,omit-frame-pointer,inline")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#include <cstdio>
#include <cstring>

static char inbuf[1 << 23];
static char grid[100005];
static char outbuf[1 << 21];
static const char* ip;

static inline int readInt() {
    while (*ip <= ' ') ip++;
    int v = 0;
    while (*ip > ' ') v = v * 10 + (*ip++ - '0');
    return v;
}

static inline char readChar() {
    while (*ip <= ' ') ip++;
    return *ip++;
}

int main() {
    size_t len = fread(inbuf, 1, sizeof(inbuf) - 1, stdin);
    inbuf[len] = 0;
    ip = inbuf;

    int tcs = readInt();
    size_t op = 0;

    while (tcs--) {
        int n = readInt(), m = readInt(), q = readInt();
        memset(grid, '.', (size_t)n * m);

        while (q--) {
            int x = readInt() - 1;
            int y = readInt() - 1;
            char c = readChar();
            int r = readInt();
            int rr = r * r;

            // dx shrinks monotonically as |dy| grows, so one pointer suffices
            int dx = r;
            for (int dy = 0; dy <= r; dy++) {
                while (dx * dx + dy * dy > rr) dx--;
                int len2 = 2 * dx + 1;
                memset(grid + (size_t)(y - dy) * m + (x - dx), c, len2);
                if (dy) memset(grid + (size_t)(y + dy) * m + (x - dx), c, len2);
            }
        }

        for (int i = 0; i < n; i++) {
            memcpy(outbuf + op, grid + (size_t)i * m, m);
            op += m;
            outbuf[op++] = '\n';
        }
        if (op > (1 << 21) - 100005 - 5) { // flush before it could overflow
            fwrite(outbuf, 1, op, stdout);
            op = 0;
        }
    }
    fwrite(outbuf, 1, op, stdout);
    return 0;
}