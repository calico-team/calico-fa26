import java.io.*;
import java.util.*;

/*
- Print a string that could be the answer string
-
- N: Length of the string
- K: Number of different -ities
- A: List containing the different -ities
*/

class Solution {
    static BufferedReader in = new BufferedReader(
        new InputStreamReader(System.in)
    );

    static PrintWriter out = new PrintWriter(System.out, true);

    static void solve(int N, int K, char[] A) throws IOException {
        // YOUR CODE HERE
    }

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());

        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().trim().split("\\s+");
            int N = Integer.parseInt(temp[0]);
            int K = Integer.parseInt(temp[1]);

            String[] tokens = in.readLine().trim().split("\\s+");
            char[] A = new char[K];

            for (int j = 0; j < K; j++) {
                A[j] = tokens[j].charAt(0);
            }

            solve(N, K, A);
        }
    }
}
