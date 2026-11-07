import java.util.*;

class Solution {

    // Helper class to represent a Drone tuple
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
    static long solve(int N, int K, List<Drone> drones) {
        long answer = 0;
        return answer;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;

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

            System.out.println(solve(N, K, drones));
        }
    }
}
