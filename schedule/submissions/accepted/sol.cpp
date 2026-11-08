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
    vector<bool> in(n, false);
    vector<vector<int>> adj(n);
    for (int i = 0; i < n; i++){
        cin >> p[i];
        p[i]--;
        if (p[i] == -1){
            in[i] = true;
        }else{
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
        if (in[i]){
            dfs(i);
            pq.push({heights[i], i});
        }
    }
    int ans = 0;
    for (int i = 0; i < m; i++){
        vector<pair<int, int>> added;
        int taken = 0;
        while (!pq.empty() && taken< k){
            auto x = pq.top();
            pq.pop();
            ans++;
            taken++;
            for (int nxt : adj[x.second]){
                added.push_back({heights[nxt], nxt});
            }
        }
        for (auto y : added){ 
            pq.push(y); 
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