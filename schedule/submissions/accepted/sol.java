import java.io.*;
import java.util.List;
import java.util.ArrayList;
import java.util.PriorityQueue;

class Solution {

    /** 
     * Return the maximum number of classes that can be taken across M semesters.
     *    
     * N: the number of classes
     * M: the number of semesters
     * K: the maximum number of classes you can take per semester
     * P: a prerequisite array for classes 1 to N (0 if there are no prerequisite classes)
     */
    public static void dfs(int x, int[] h, List<List<Integer>> adj) {
        h[x] = 0;
        for (int nxt : adj.get(x)){
            dfs(nxt, h, adj);
            h[x] = Integer.max(h[nxt]+1, h[x]);
        }
    }

    public static void solve() throws IOException {
        String[] temp = sysin.readLine().split(" ");
        int n = Integer.parseInt(temp[0]);
        int m = Integer.parseInt(temp[1]);
        int k = Integer.parseInt(temp[2]);
        
        int[] p = new int[n];
        int[] h = new int[n];
        Boolean[] in = new Boolean[n];
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++){
            adj.add(new ArrayList<>());
        }
        temp = sysin.readLine().split(" ");
        for (int i = 0; i < n; i++){
            p[i] = Integer.parseInt(temp[i]);
            p[i]--;
            if (p[i] == -1){
                in[i] = true;
            }else{
                in[i] = false;
                adj.get(p[i]).add(i);
            }
        }
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(b[1], a[1]));
        for (int i = 0; i < n; i++){
            if (in[i]){
                dfs(i, h, adj);
                pq.add(new int[]{i, h[i]});
            }
        }
        int ans = 0;
        for (int i = 0; i < m; i++){
            List<Integer> added = new ArrayList<>();
            int taken = 0;
            while (!pq.isEmpty() && taken < k){
                int[] x = pq.poll();
                ans++;
                taken++;
                for (int nxt : adj.get(x[0])){
                    added.add(nxt);
                }
            }
            for (int x : added){
                pq.add(new int[]{x, h[x]});
            }
        }
        sysout.println(ans);
    }

    static BufferedReader sysin = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter sysout = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    public static void main(String[] args) throws IOException{ 
        int T = Integer.parseInt(sysin.readLine());
        for (int t = 0; t < T; t++) {
            solve();
        }
        sysout.flush();
    }

}