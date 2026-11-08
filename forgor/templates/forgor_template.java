import java.io.*;

class Solution {
    /**
    * Phase 1: encode the tree.
    *
    * N: the number of vertices
    * E: the N - 1 edges of the tree as (u, v) pairs, in arbitrary
    *    order — not necessarily lexicographically increasing, and u
    *    is not guaranteed to be the parent of v
    * Returns: the N integers A_1..A_N, your encoding of the tree
    */
    static int[] solve_phase1(int N, int[][] E) {
        // YOUR CODE HERE
        return new int[N];
    }

    /**
    * Phase 2: recover the tree from your own encoding.
    *
    * N: the number of vertices
    * A: the N integers A_1..A_N — identical to what your phase 1 output
    *    for this test case, with exactly one value replaced by -1 (the
    *    erased value)
    * Returns: the N - 1 edges of the original tree as (u, v) pairs,
    *          one edge per output line (the checker compares the set
    *          of edges, so the order and orientation of the pairs do
    *          not matter)
    */
    static int[][] solve_phase2(int N, int[] A) {
        // YOUR CODE HERE
        return new int[0][2];
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        String phase = in.readLine().trim();
        int N = Integer.parseInt(in.readLine().trim());

        if (phase.equals("FIRST")) {
            int[][] E = new int[N - 1][2];
            for (int i = 0; i < N - 1; i++) {
                String[] temp = in.readLine().trim().split(" ");
                E[i][0] = Integer.parseInt(temp[0]);
                E[i][1] = Integer.parseInt(temp[1]);
            }
            int[] A = solve_phase1(N, E);
            for (int i = 0; i < N; i++) {
                if (i > 0) out.print(' ');
                out.print(A[i]);
            }
            out.println();
        } else {
            String[] temp = in.readLine().trim().split(" ");
            int[] A = new int[N];
            for (int i = 0; i < N; i++) {
                A[i] = Integer.parseInt(temp[i]);
            }
            int[][] edges = solve_phase2(N, A);
            for (int i = 0; i < edges.length; i++) {
                out.println(edges[i][0] + " " + edges[i][1]);
            }
        }
        out.flush();
    }
}
