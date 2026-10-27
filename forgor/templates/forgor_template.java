import java.io.*;

class Solution {
    /**
    * Phase 1: encode the tree.
    *
    * N: the number of vertices
    * P: the parent array of the tree: P[i] is the parent of vertex i + 1,
    *    or i + 1 if vertex i + 1 has no parent (the root).
    * Returns: the N integers A_1..A_N, your encoding of the tree.
    */
    static int[] solve_phase1(int N, int[] P) {
        // YOUR CODE HERE
        return new int[N];
    }

    /**
    * Phase 2: recover the tree from your own encoding.
    *
    * N: the number of vertices
    * A: the N integers A_1..A_N — identical to what your phase 1 output
    *    for this test case, with exactly one value replaced by -1 (the
    *    erased value).
    * Returns: the N integers P_1..P_N, the parent array of the original
    *          tree (P[i] is the parent of vertex i + 1, or i + 1 if
    *          vertex i + 1 has no parent).
    */
    static int[] solve_phase2(int N, int[] A) {
        // YOUR CODE HERE
        return new int[N];
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        String[] first = in.readLine().split(" ");
        int T = Integer.parseInt(first[0]);
        int phase = Integer.parseInt(first[1]);

        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(in.readLine());
            String[] line = in.readLine().split(" ");

            int[] A = new int[N];
            int[] P = new int[N];
            if (phase == 1) {
                for (int j = 0; j < N; j++) {
                    P[j] = Integer.parseInt(line[j]);
                }
                A = solve_phase1(N, P);
            } else {
                for (int j = 0; j < N; j++) {
                    A[j] = Integer.parseInt(line[j]);
                }
                P = solve_phase2(N, A);
            }

            int[] result = (phase == 1) ? A : P;
            for (int j = 0; j < N; j++) {
                if (j > 0) out.print(' ');
                out.print(result[j]);
            }
            out.println();
        }
        out.flush();
    }
}
