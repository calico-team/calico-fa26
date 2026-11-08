#include <bits/stdc++.h>

using namespace std;

static char input_buffer[1 << 25];
size_t input_pos = 0, input_len = 0;

int read_int() {
    while (input_pos < input_len && (input_buffer[input_pos] < '0' || input_buffer[input_pos] > '9')) input_pos++;
    int x = 0;
    while (input_pos < input_len && input_buffer[input_pos] >= '0' && input_buffer[input_pos] <= '9') {
        x = x * 10 + (input_buffer[input_pos++] - '0');
    }
    return x;
}

void read_row(char* dst, int M) {
    while (input_buffer[input_pos] != '.' && input_buffer[input_pos] != 'R' && input_buffer[input_pos] != 'B') input_pos++;
    memcpy(dst, input_buffer + input_pos, M);
    input_pos += M;
}

int main() {
    input_len = fread(input_buffer, 1, sizeof(input_buffer), stdin);
    string out;
    int T = read_int();
    while (T--) {
        int N = read_int(), M = read_int(), Q = read_int();
        int W = M + 2, H = N + 2, P = W * H;

        vector<char> grid(P, '#');
        for (int r = 0; r < N; r++) read_row(&grid[(r + 1) * W + 1], M);

        vector<unsigned char> blocked(2 * P);
        for (int c = 0; c < P; c++) {
            blocked[c] = !(grid[c] == '.' || grid[c] == 'R');
            blocked[P + c] = !(grid[c] == '.' || grid[c] == 'B');
        }
        int dirs[4] = {1, -1, W, -W};

        vector<int> comp(2 * P, -1), bfs_queue(2 * P);
        int comps = 0;
        for (int s = 0; s < 2 * P; s++) {
            if (blocked[s] || comp[s] != -1) continue;
            int head = 0, tail = 0;
            comp[s] = comps;
            bfs_queue[tail++] = s;
            while (head < tail) {
                int u = bfs_queue[head++];
                int other = u >= P ? u - P : u + P;
                if (!blocked[other] && comp[other] == -1) {
                    comp[other] = comps;
                    bfs_queue[tail++] = other;
                }
                for (int k = 0; k < 4; k++) {
                    int v = u + dirs[k];
                    if (!blocked[v] && comp[v] == -1) {
                        comp[v] = comps;
                        bfs_queue[tail++] = v;
                    }
                }
            }
            comps++;
        }

        vector<int> start_cell(Q), end_cell(Q), K(Q);
        vector<char> answer(Q, 0), pending(Q, 0);
        for (int q = 0; q < Q; q++) {
            int sr = read_int(), sc = read_int(), er = read_int(), ec = read_int();
            K[q] = read_int();
            start_cell[q] = (sr + 1) * W + sc + 1;
            end_cell[q] = (er + 1) * W + ec + 1;
            int source_comp = comp[P + start_cell[q]];
            bool reachable = comp[end_cell[q]] == source_comp || comp[P + end_cell[q]] == source_comp;
            pending[q] = reachable && K[q] >= abs(sr - er) + abs(sc - ec);
        }

        vector<int> seen_start(P, 0), seen_end(P, 0);
        int distinct_starts = 0, distinct_ends = 0;
        for (int q = 0; q < Q; q++) {
            if (!pending[q]) continue;
            if (!seen_start[start_cell[q]]++) distinct_starts++;
            if (!seen_end[end_cell[q]]++) distinct_ends++;
        }
        bool by_end = distinct_ends < distinct_starts;

        vector<int> group_start(P + 1, 0), order(Q);
        for (int q = 0; q < Q; q++) {
            if (pending[q]) group_start[(by_end ? end_cell[q] : start_cell[q]) + 1]++;
        }
        for (int c = 0; c < P; c++) group_start[c + 1] += group_start[c];
        vector<int> fill_pos(group_start.begin(), group_start.end() - 1);
        for (int q = 0; q < Q; q++) {
            if (pending[q]) order[fill_pos[by_end ? end_cell[q] : start_cell[q]]++] = q;
        }

        vector<unsigned char> visited(2 * P);
        vector<unsigned> wanted(2 * P, 0), found(P, 0);
        vector<int> found_dist(P);
        unsigned stamp = 0;
        for (int key = 0; key < P; key++) {
            int lo = group_start[key], hi = group_start[key + 1];
            if (lo == hi) continue;
            stamp++;
            int remaining = 0, max_k = 0;
            for (int i = lo; i < hi; i++) {
                int q = order[i];
                max_k = max(max_k, K[q]);
                if (by_end) {
                    int t = P + start_cell[q];
                    if (wanted[t] != stamp) {
                        wanted[t] = stamp;
                        remaining++;
                    }
                } else {
                    int t = end_cell[q];
                    if (wanted[t] != stamp) {
                        wanted[t] = stamp;
                        wanted[P + t] = stamp;
                        remaining++;
                    }
                }
            }

            memcpy(visited.data(), blocked.data(), 2 * P);
            int head = 0, tail = 0;
            if (by_end) {
                if (!visited[key]) {
                    visited[key] = 1;
                    bfs_queue[tail++] = key;
                }
                if (!visited[P + key]) {
                    visited[P + key] = 1;
                    bfs_queue[tail++] = P + key;
                }
            } else {
                visited[P + key] = 1;
                bfs_queue[tail++] = P + key;
            }

            for (int d = 0; head < tail && remaining > 0 && d <= max_k; d++) {
                int layer_end = tail;
                while (head < layer_end) {
                    int u = bfs_queue[head++];
                    if (wanted[u] == stamp) {
                        int c = u >= P ? u - P : u;
                        wanted[c] = 0;
                        wanted[P + c] = 0;
                        found[c] = stamp;
                        found_dist[c] = d;
                        if (--remaining == 0) break;
                    }
                    int other = u >= P ? u - P : u + P;
                    if (!visited[other]) {
                        visited[other] = 1;
                        bfs_queue[tail++] = other;
                    }
                    for (int k = 0; k < 4; k++) {
                        int v = u + dirs[k];
                        if (!visited[v]) {
                            visited[v] = 1;
                            bfs_queue[tail++] = v;
                        }
                    }
                }
            }

            for (int i = lo; i < hi; i++) {
                int q = order[i];
                int t = by_end ? start_cell[q] : end_cell[q];
                answer[q] = found[t] == stamp && found_dist[t] <= K[q];
            }
        }

        for (int q = 0; q < Q; q++) out += answer[q] ? "YES\n" : "NO\n";
    }
    fwrite(out.data(), 1, out.size(), stdout);
}
