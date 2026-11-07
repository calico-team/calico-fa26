#include <bits/stdc++.h>
using namespace std;

/*
* Return an integer denoting the amount of rain collected after the Kth nights
* 
* N: Number of drones
* K: Number of nights
* drone: a tuple in this order {x_coordinate, y_coordinate, z_coordinate, direction} for each drone
*/

long long solve(int N, int K, vector<tuple<int, int, int, char>> drones){
    long long answer =0;

    return answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
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
