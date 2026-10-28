import java.io.*;

class Solution {

    /*
     * Output whether all of the requests can be fulfilled.
     *
     * N: Number of smoke requests
     * R: Number of seconds needed for a smoke charge to recharge
     * A: List of timestamps where smokes are requested
     */
    static String solve(int N, int R, int[] A) {
        int charges = 2;
        int cooldown = R;
        int idx = 0;
        for (int t = 0; t < A[N - 1]; t++) {
            if (charges == 2) {
                cooldown = R;
            }
            else {
                cooldown--;
                if (cooldown == 0) {
                    cooldown = R;
                    charges++;
                }
                if (A[idx] == t) {
                    if (charges == 0) {
                        return "NO";
                    }
                    else {
                        charges--;
                        idx++;
                    }
                }
            }
        }
        return "YES";
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