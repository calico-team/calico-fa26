#include <iostream>
#include <vector>
#include <queue>
#include <functional>
using namespace std;
typedef long long ll;

void solve(){
    int n, m, k;
    cin >> n >> m >> k;
    vector<int> p(n), heights(n, -1);
    vector<vector<int>> adj(n);
    for (int i = 0; i < n; i++){
        cin >> p[i];
        p[i]--;
        if (p[i] != -1){
            adj[p[i]].push_back(i);
        }
    }
    priority_queue<pair<int, int>> pq;
    function<void(int)> dfs = [&](int x){
        heights[x] = 0;
        for (int nxt : adj[x]){
            dfs(nxt);
            heights[x] = max(heights[nxt]+1, heights[x]);
        }
    };
    for (int i = 0; i < n; i++){
        if (p[i] == -1){
            // dfs(i);
            pq.push({adj[i].size(), i});
        }
    }
    int ans = 0;
    for (int i = 0; i < m; i++){
        vector<int> added;
        int taken = 0;
        while (!pq.empty() && taken< k){
            auto x = pq.top();
            pq.pop();
            ans++;
            taken++;
            for (int nxt : adj[x.second]){
                added.push_back(nxt);
            }
        }
        for (int y : added){ 
            pq.push({adj[y].size(), y}); 
        }
    }
    cout << ans << "\n";
}

int main(){
    int t;
    cin >> t;
    while (t--){
        solve();
    }
}