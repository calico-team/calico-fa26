import java.util.*;

class Solution {
    /*
    - Output YES or NO for all the queries
    - N: Number of rows
    - M: Number of columns
    - Q: Number of queries
    - start: List/array of starting coordinates for each query (0-indexed or 1-indexed as read)
    - end: List/array of ending coordinates for each query (0-indexed or 1-indexed as read)
    */
    static List<String> solve(int N, int M, int Q, String[] G, int[][] start, int[][] end) {
        List<String> ans = new ArrayList<>();
        return ans;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;

        int T = sc.nextInt();
        for (int i = 0; i < T; i++) {
            int N = sc.nextInt();
            int M = sc.nextInt();
            int Q = sc.nextInt();

            String[] G = new String[N];
            for (int j = 0; j < N; j++) {
                G[j] = sc.next();
            }

            int[][] start = new int[Q][2];
            int[][] end = new int[Q][2];

            for (int j = 0; j < Q; j++) {
                start[j][0] = sc.nextInt();
                start[j][1] = sc.nextInt();
                end[j][0] = sc.nextInt();
                end[j][1] = sc.nextInt();
            }

            List<String> result = solve(N, M, Q, G, start, end);
            for (String s : result) {
                System.out.println(s);
            }
        }
    }
}