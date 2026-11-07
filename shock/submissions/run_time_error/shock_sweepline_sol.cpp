#include <iostream>
#include <vector>
#include <set>
using namespace std;

struct RowQuake { // think of an earthquake as many RowQuakes each affecting only one row
    int centerX; // same as the center x of the earthquake this RowQuake is from
    int centerShock; // the maximum amount of shock achieved in this row by the source earthquake. that is, the shock at centerX
};

void solve(){
    int n, m, q;
    cin>>n>>m>>q;
    bool swapDimensions = (n > m);
    if(swapDimensions){
        swap(n, m);
    }
    vector<vector<vector<int>>> startTimes(n,vector<vector<int>>(m+1)), endTimes(n,vector<vector<int>>(m+1));

    vector<int> xs, ys, rs;
    for(int globalTime = 0; globalTime<q; globalTime++){
        int x, y, r;
        cin>>x>>y>>r;
        x--; y--;
        if(swapDimensions){
            swap(x, y);
        }
        xs.push_back(x);
        ys.push_back(y);
        rs.push_back(r);

        // go through first quadrant of the circle (go top down, see how far right you have to mark the ends)
        int borderX = x;
        for(int borderY = y - r; borderY <= y; borderY++){ // we'll double paint the horizontal diameter but that's fine (the map will actually forget about that anyway)
            while((borderX-x)*(borderX-x) + (borderY-y)*(borderY-y) <= r*r){ // this while loop could just be replaced with square root math
                borderX++;
            }
            borderX--;
            // borderX is now as far right as possible while still being in/on the circle
            startTimes[borderY][x-(borderX-x)].push_back(globalTime);
            endTimes[borderY][borderX+1].push_back(globalTime);
            startTimes[y+(y-borderY)][x-(borderX-x)].push_back(globalTime);
            endTimes[y+(y-borderY)][borderX+1].push_back(globalTime);
        }
    }

    vector<vector<int>> answer(n, vector<int>(m, 0));
    for(int y = 0; y < n; y++){
        set<int> current; // contains all the times corresponding to earthquakes that affected the position we are looking at
        for(int x = 0; x < m; x++){
            for(auto& startTime : startTimes[y][x]){
                current.insert(startTime);
            }
            for(auto& endTime : endTimes[y][x]){
                current.erase(endTime);
            }
            if(current.size()){
                int time = *current.rbegin();
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
    int tcs;
    cin>>tcs;
    while(tcs--){
        solve();
    }
}