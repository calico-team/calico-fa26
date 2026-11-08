import java.io.*;
import java.util.*;

class Solution {

    /*
     * Output whether all of the requests can be fulfilled.
     *
     * N: Number of smoke requests
     * R: Number of seconds needed for a smoke charge to recharge
     * A: List of timestamps where smokes are requested
     */
    static String solve(int N, int R, int[] A) {
        ArrayList<Integer> recharging = new ArrayList<>();
        for (int a : A) {
            while (!recharging.isEmpty() && recharging.get(0) <= a) {
                recharging.remove(0);
            }

            if (recharging.size() == 2) {
                return "NO";
            } else if (recharging.size() == 1) {
                recharging.add(recharging.get(0) + R);
            } else {
                recharging.add(a + R);
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