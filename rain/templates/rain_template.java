import java.io.*;

class Solution {
    /**
    * Return the total units of rain collected over the K nights.
    *
    * N: the number of drones
    * X: the starting x coordinate of each drone
    * Y: the starting y coordinate of each drone
    * Z: the starting z coordinate of each drone
    * DIR: the direction of each drone, one of "N" or "E"
    * K: the number of nights
    */
    static long solve(int N, int[] X, int[] Y, int[] Z, String[] DIR, long K) {
        // YOUR CODE HERE
        return -1;
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());

        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int N = Integer.parseInt(temp[0]);
            long K = Long.parseLong(temp[1]);

            int[] X = new int[N];
            int[] Y = new int[N];
            int[] Z = new int[N];
            String[] DIR = new String[N];
            for (int j = 0; j < N; j++) {
                String[] drone = in.readLine().split(" ");
                X[j] = Integer.parseInt(drone[0]);
                Y[j] = Integer.parseInt(drone[1]);
                Z[j] = Integer.parseInt(drone[2]);
                DIR[j] = drone[3];
            }

            out.println(solve(N, X, Y, Z, DIR, K));
        }
        out.flush();
    }
}
