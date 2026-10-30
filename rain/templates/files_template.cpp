#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

int solve(int N, int K, vector<tuple<int, int, int, char>> drones){
    int answer =0;

    return answer; 
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int t; cin>>t;
    while (t--){
        int N, K; cin>>N>>K;
        vector<tuple<int, int, int, char>> drones;
        for (int i = 0; i < N; i++){
            int x, y, z;
            char d;
            cin>>x>>y>>z>>d;
            drones.push_back({x, y, z, d});
        }
        cout<<solve(N, K, drones)<<endl;
    }
}