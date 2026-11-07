import java.io.*;
import java.util.*;

class Solution {
    static class Drone {
        int x, y, z;
        char direction;

        Drone(int x, int y, int z, char direction) {
            this.x = x;
            this.y = y;
            this.z = z;
            this.direction = direction;
        }
    }

    /*
    - Return an integer denoting the amount of rain collected after the Kth nights
    - 
    - N: Number of drones
    - K: Number of nights
    - drones: List of Drone objects containing {x, y, z, direction}
    */
    static int solve(int N, int K, List<Drone> drones) {
        int answer = 0;
        return answer;
    }
    public static void main(String[] args) throws IOException {
        FastScanner sc = new FastScanner();
        PrintWriter out = new PrintWriter(System.out);

        if (!sc.hasNext()) {
            out.flush();
            return;
        }

        int T = sc.nextInt();
        while (T-- > 0) {
            int N = sc.nextInt();
            int K = sc.nextInt();

            List<Drone> drones = new ArrayList<>();
            for (int i = 0; i < N; i++) {
                int x = sc.nextInt();
                int y = sc.nextInt();
                int z = sc.nextInt();
                char d = sc.next().charAt(0);
                drones.add(new Drone(x, y, z, d));
            }

            out.println(solve(N, K, drones));
        }

        out.flush();
    }

    static class FastScanner {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    String line = br.readLine();
                    if (line == null) return null;
                    st = new StringTokenizer(line);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        boolean hasNext() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    String line = br.readLine();
                    if (line == null) return false;
                    st = new StringTokenizer(line);
                } catch (IOException e) {
                    return false;
                }
            }
            return true;
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
    }
}