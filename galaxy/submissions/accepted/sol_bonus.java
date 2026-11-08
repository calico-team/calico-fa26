import java.io.*;

class Solution {
    static class DSU {
        int[] parent, size;

        DSU(int n) {
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        int find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        boolean connect(int a, int b) {
            a = find(a);
            b = find(b);
            if (a == b) return false;
            if (size[a] < size[b]) {
                int tmp = a;
                a = b;
                b = tmp;
            }
            parent[b] = a;
            size[a] += size[b];
            return true;
        }

        boolean isConnected(int a, int b) {
            return find(a) == find(b);
        }
    }

    static String[] solve(int N, int M, int Q, String[] G, int[][] start, int[][] end) {
        DSU dsu = new DSU(N*M);
        int[][] dirs = {{-1,0}, {1,0}, {0,-1}, {0,1}};
        for (int row = 0; row < N; row++) {
            for (int col = 0; col < M; col++) {
                for (int[] dir : dirs) {
                    int dr = dir[0], dc = dir[1];
                    if (row+dr >= 0 && row+dr < N && col+dc >= 0 && col+dc < M) {
                        char cur = G[row].charAt(col);
                        char nxt = G[row+dr].charAt(col+dc);
                        if (cur == nxt || cur == '.' || nxt == '.') {
                            dsu.connect(row*M+col, (row+dr)*M+(col+dc));
                        }
                    }
                }
            }
        }

        String[] ans = new String[Q];
        for (int i = 0; i < Q; i++) {
            int startRow = start[i][0], startCol = start[i][1];
            int endRow = end[i][0], endCol = end[i][1];
            ans[i] = dsu.isConnected(startRow*M+startCol, endRow*M+endCol) ? "YES" : "NO";
        }
        return ans;
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
            for (int i = 0; i < Q; i++) {
                temp = in.readLine().trim().split(" ");
                start[i][0] = Integer.parseInt(temp[0]);
                start[i][1] = Integer.parseInt(temp[1]);
                end[i][0] = Integer.parseInt(temp[2]);
                end[i][1] = Integer.parseInt(temp[3]);
            }

            for (String s : solve(N, M, Q, G, start, end)) {
                out.println(s);
            }
        }
        out.flush();
    }
}
