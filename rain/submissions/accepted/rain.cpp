// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

template <typename T>
using ordered_set = tree<
    T,
    null_type,
    less<T>,
    rb_tree_tag,
    tree_order_statistics_node_update
>;

#define f first
#define s second

typedef long long int ll;


int main() {
    int T;
    cin>>T;
    while(T--){
        int n, k;
        cin>>n>>k;
        //           z        x   y   east?
        vector<pair<int,tuple<int,int,bool>>> drones;
        for(int i = 0; i<n; ++i){
            int x,y,z;
            char d;
            cin>>x>>y>>z>>d;
            drones.push_back({-z,{x,y,d=='E'}});
        }

        sort(drones.begin(),drones.end());

        //            x+y        x pos
        unordered_map<int, ordered_set<int>> eastDrones;
        unordered_map<int, ordered_set<int>> northDrones;

        ll ret = 1LL * k * n;

        for(auto drone : drones){
            int x = get<0>(drone.s);
            int y = get<1>(drone.s);
            bool east = get<2>(drone.s);
            if(east){

                if(northDrones.contains(x+y)){
                    ordered_set<int> &a = northDrones[x+y];
                    ret -= a.order_of_key(x+k) - a.order_of_key(x);
                }


                eastDrones[x+y].insert(x);
            }else{

                if(eastDrones.contains(x+y)){
                    ordered_set<int> &a = eastDrones[x+y];
                    ret -= a.order_of_key(x+1) - a.order_of_key(x-k+1);
                }


                northDrones[x+y].insert(x);
            }

        }

        cout<<ret<<endl;
    }


}