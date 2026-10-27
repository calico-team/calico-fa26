import java.io.*;

class Solution {
    /**
    * Return whether Ben can reach the bottom-right tile of the grid.
    *
    * N: the number of rows in the grid
    * M: the number of columns in the grid
    * G: the grid, where G[i] is the i-th row and each character is one of
    *    'R', 'B', or '.'
    */
    static String solve(int N, int M, String[] G) {
        // YOUR CODE HERE
        return "";
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());

        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int N = Integer.parseInt(temp[0]);
            int M = Integer.parseInt(temp[1]);

            String[] G = new String[N];
            for (int j = 0; j < N; j++) {
                G[j] = in.readLine();
            }

            out.println(solve(N, M, G));
        }
        out.flush();
    }
}
