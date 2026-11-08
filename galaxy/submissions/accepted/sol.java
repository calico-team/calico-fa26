import java.io.*;
import java.util.*;

class Solution {
    static String[] solve(int N, int M, int Q, String[] G, int[][] start, int[][] end) {
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{N-1, M-1});
        boolean[][] visited = new boolean[N][M];
        visited[N-1][M-1] = true;
        int[][] dirs = {{-1,0}, {1,0}, {0,-1}, {0,1}};
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int row = cell[0], col = cell[1];
            for (int[] dir : dirs) {
                int dr = dir[0], dc = dir[1];
                if (row+dr >= 0 && row+dr < N && col+dc >= 0 && col+dc < M) {
                    char cur = G[row].charAt(col);
                    char nxt = G[row+dr].charAt(col+dc);
                    if (!visited[row+dr][col+dc] && (cur == nxt || cur == '.' || nxt == '.')) {
                        visited[row+dr][col+dc] = true;
                        queue.add(new int[]{row+dr, col+dc});
                    }
                }
            }
        }

        String[] ans = new String[Q];
        for (int i = 0; i < Q; i++) {
            ans[i] = visited[start[i][0]][start[i][1]] ? "YES" : "NO";
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
