#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
using namespace std;

void solve(){
    int n, m, q;
    cin>>n>>m>>q;
    bool swapDimensions = (n > m);
    if(swapDimensions){
        swap(n, m);
    }

    vector<int> xs(q), ys(q), rs(q);
    for(int globalTime = 0; globalTime < q; globalTime++){
        int y, x, r;
        cin>>y>>x>>r;
        if(swapDimensions){
            swap(x, y);
        }
        xs[globalTime] = x;
        ys[globalTime] = y;
        rs[globalTime] = r;
    }

    // only one row's worth of events exists at a time
    vector<vector<int>> startTimes(m+1), endTimes(m+1);
    vector<vector<int>> answer(n, vector<int>(m, 0));

    for(int y = 0; y < n; y++){
        for(auto& v : startTimes) v.clear();
        for(auto& v : endTimes) v.clear();

        // build this row's events from every earthquake that reaches it
        for(int t = 0; t < q; t++){
            int dy = y - ys[t];
            int r = rs[t];
            if(dy < -r || dy > r) continue;
            int rem = r*r - dy*dy;
            int w = (int)sqrt((double)rem);
            while(w*w > rem) w--;
            while((w+1)*(w+1) <= rem) w++;
            startTimes[xs[t]-w].push_back(t);
            endTimes[xs[t]+w+1].push_back(t);
        }

        priority_queue<int> current;
        vector<bool> toDelete(q,false);
        for(int x = 0; x < m; x++){
            for(auto& startTime : startTimes[x]){
                current.push(startTime);
            }
            for(auto& endTime : endTimes[x]){
                toDelete[endTime] = true;
            }
            while(current.size() && toDelete[current.top()]){
                toDelete[current.top()] = false;
                current.pop();
            }
            if(current.size()){
                int time = current.top();
                answer[y][x] = rs[time]*rs[time] - ((x-xs[time])*(x-xs[time]) + (y-ys[time])*(y-ys[time])) + 1;
            }
        }
    }

    if(swapDimensions){
        for(int x = 0; x < m; x++){
            for(int y = 0; y < n; y++){
                cout<<answer[y][x]<<' ';
            }
            cout<<'\n';
        }
    }
    else{
        for(int y = 0; y < n; y++){
            for(int x = 0; x < m; x++){
                cout<<answer[y][x]<<' ';
            }
            cout<<'\n';
        }
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int tcs;
    cin>>tcs;
    while(tcs--){
        solve();
    }
}