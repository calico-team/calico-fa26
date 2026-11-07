#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int MXN = 100000;

vector<pair<int, char>> at[MXN * 2 + 1];

/*
* Return an integer denoting the amount of rain collected after the Kth nights
* 
* N: Number of drones
* K: Number of nights
* drone: a tuple in this order {x_coordinate, y_coordinate, z_coordinate, direction} for each drone
*/ 
long long solve(int N, int K, vector<tuple<int, int, int, char>> drones){
	vector<int> idxs;
	for (auto& i : drones) {
		at[get<0>(i) + get<1>(i)].push_back({get<0>(i), get<3>(i)});
		idxs.push_back(get<0>(i) + get<1>(i));
	}
	sort(idxs.begin(), idxs.end());
	idxs.erase(unique(idxs.begin(), idxs.end()), idxs.end());
	ll ans = (ll) N * K;
	for (int i : idxs) {
		sort(at[i].begin(), at[i].end());
		deque<int> dq;
		for (pair<int, char>& j : at[i]) {
			if (j.second == 'E') {
				dq.push_back(j.first);
			} else {
				while (!dq.empty() && j.first - dq.front() >= K) dq.pop_front();
				ans -= dq.size();
			}
		}
	}
	for (int i : idxs) {
		at[i].clear();
	}
	return ans;
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
