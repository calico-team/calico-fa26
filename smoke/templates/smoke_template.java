import java.io.*;

class Solution {
    /**
    * Return whether Omen can throw a smoke for every teammate request.
    *
    * N: the number of requests
    * R: the number of seconds it takes for a smoke to recharge
    * A: the times (in seconds) at which each request is made
    */
    static String solve(int N, int R, int[] A) {
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
            int R = Integer.parseInt(temp[1]);

            int[] A = new int[N];
            String[] req = in.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                A[j] = Integer.parseInt(req[j]);
            }

            out.println(solve(N, R, A));
        }
        out.flush();
    }
}
