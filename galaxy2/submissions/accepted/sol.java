import java.io.*;
import java.util.*;

class Solution {
    static final int INF = Integer.MAX_VALUE / 2;
    static final int[] DR = {-1, 1, 0, 0};
    static final int[] DC = {0, 0, -1, 1};

    static int rows, cols;
    static String[] grid;
    static int[][] starts, ends;
    static int[] dist, ans, queue;

    static String[] solve(int N, int M, int Q, String[] G, int[][] start, int[][] end, int[] K) {
        rows = N;
        cols = M;
        grid = G;
        starts = start;
        ends = end;
        dist = new int[N * M * 2];
        queue = new int[N * M * 2];
        ans = new int[Q];
        Arrays.fill(ans, INF);

        int[] qs = new int[Q];
        for (int q = 0; q < Q; q++) {
            qs[q] = q;
        }
        divide(0, N - 1, 0, M - 1, qs);

        String[] res = new String[Q];
        for (int q = 0; q < Q; q++) {
            res[q] = ans[q] <= K[q] ? "YES" : "NO";
        }
        return res;
    }

    static int id(int r, int c, int s) {
        return (r * cols + c) * 2 + s;
    }

    static boolean valid(int r, int c, int s) {
        char ch = grid[r].charAt(c);
        return ch == '.' || ch == "RB".charAt(s);
    }

    static void bfs(int r0, int r1, int c0, int c1, int sr, int sc, int ss) {
        for (int r = r0; r <= r1; r++) {
            for (int c = c0; c <= c1; c++) {
                dist[id(r, c, 0)] = INF;
                dist[id(r, c, 1)] = INF;
            }
        }
        int head = 0, tail = 0;
        dist[id(sr, sc, ss)] = 0;
        queue[tail++] = id(sr, sc, ss);
        while (head < tail) {
            int u = queue[head++];
            int r = u / 2 / cols, c = u / 2 % cols, s = u % 2;
            int d = dist[u];
            if (grid[r].charAt(c) == '.' && dist[id(r, c, 1 - s)] == INF) {
                dist[id(r, c, 1 - s)] = d + 1;
                queue[tail++] = id(r, c, 1 - s);
            }
            for (int k = 0; k < 4; k++) {
                int nr = r + DR[k], nc = c + DC[k];
                if (nr >= r0 && nr <= r1 && nc >= c0 && nc <= c1 && valid(nr, nc, s) && dist[id(nr, nc, s)] == INF) {
                    dist[id(nr, nc, s)] = d + 1;
                    queue[tail++] = id(nr, nc, s);
                }
            }
        }
    }

    static void divide(int r0, int r1, int c0, int c1, int[] qs) {
        if (r0 > r1 || c0 > c1 || qs.length == 0) {
            return;
        }
        boolean splitCol = c1 - c0 >= r1 - r0;
        int mid = splitCol ? (c0 + c1) / 2 : (r0 + r1) / 2;
        int len = splitCol ? r1 - r0 + 1 : c1 - c0 + 1;

        for (int i = 0; i < len; i++) {
            int r = splitCol ? r0 + i : mid;
            int c = splitCol ? mid : c0 + i;
            for (int s = 0; s < 2; s++) {
                if (!valid(r, c, s)) continue;
                bfs(r0, r1, c0, c1, r, c, s);
                for (int q : qs) {
                    int toStart = dist[id(starts[q][0], starts[q][1], 1)];
                    int toEnd = Math.min(dist[id(ends[q][0], ends[q][1], 0)], dist[id(ends[q][0], ends[q][1], 1)]);
                    ans[q] = Math.min(ans[q], toStart + toEnd);
                }
            }
        }

        int[] first = new int[qs.length], second = new int[qs.length];
        int firstCount = 0, secondCount = 0;
        for (int q : qs) {
            int a = splitCol ? starts[q][1] : starts[q][0];
            int b = splitCol ? ends[q][1] : ends[q][0];
            if (a < mid && b < mid) first[firstCount++] = q;
            if (a > mid && b > mid) second[secondCount++] = q;
        }
        if (splitCol) {
            divide(r0, r1, c0, mid - 1, Arrays.copyOf(first, firstCount));
            divide(r0, r1, mid + 1, c1, Arrays.copyOf(second, secondCount));
        } else {
            divide(r0, mid - 1, c0, c1, Arrays.copyOf(first, firstCount));
            divide(mid + 1, r1, c0, c1, Arrays.copyOf(second, secondCount));
        }
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine().trim());
        for (int t = 0; t < T; t++) {
            String[] temp = in.readLine().trim().split(" ");
            int N = Integer.parseInt(temp[0]);
            int M = Integer.parseInt(temp[1]);
            int Q = Integer.parseInt(temp[2]);
            String[] G = new String[N];
            for (int i = 0; i < N; i++) {
                G[i] = in.readLine().trim();
            }
            int[][] start = new int[Q][2];
            int[][] end = new int[Q][2];
            int[] K = new int[Q];
            for (int i = 0; i < Q; i++) {
                temp = in.readLine().trim().split(" ");
                start[i][0] = Integer.parseInt(temp[0]);
                start[i][1] = Integer.parseInt(temp[1]);
                end[i][0] = Integer.parseInt(temp[2]);
                end[i][1] = Integer.parseInt(temp[3]);
                K[i] = Integer.parseInt(temp[4]);
            }

            for (String s : solve(N, M, Q, G, start, end, K)) {
                out.println(s);
            }
        }
        out.flush();
    }
}
