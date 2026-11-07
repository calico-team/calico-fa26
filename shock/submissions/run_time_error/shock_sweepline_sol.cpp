#include <iostream>
#include <vector>
#include <map>
using namespace std;

struct RowQuake { // think of an earthquake as many RowQuakes each affecting only one row
    int centerX; // same as the center x of the earthquake this RowQuake is from
    int centerShock; // the maximum amount of shock achieved in this row by the source earthquake. that is, the shock at centerX
};
struct Start{
    int time;
    RowQuake rowQuake;
};

void solve(){
    int n, m, q;
    cin>>n>>m>>q;
    bool swapDimensions = (n > m);
    if(swapDimensions){
        swap(n, m);
    }
    vector<vector<vector<Start>>> starts(n,vector<vector<Start>>(m+1)); // a 2D grid of lists of points of interest (each row is 1 longer than length m because the ending starts are exclusive)
    vector<vector<vector<int>>> endTimes(n,vector<vector<int>>(m+1));

    for(int globalTime = 0; globalTime<q; globalTime++){
        int x, y, r;
        cin>>x>>y>>r;
        x--; y--;
        if(swapDimensions){
            swap(x, y);
        }

        // go through first quadrant of the circle (go top down, see how far right you have to mark the ends)
        int borderX = x;
        for(int borderY = y - r; borderY <= y; borderY++){ // we'll double paint the horizontal diameter but that's fine (the map will actually forget about that anyway)
            while((borderX-x)*(borderX-x) + (borderY-y)*(borderY-y) <= r*r){ // this while loop could just be replaced with square root math
                borderX++;
            }
            borderX--;
            // borderX is now as far right as possible while still being in/on the circle
            starts[borderY][x-(borderX-x)].push_back({globalTime,{x,r*r-(borderY-y)*(borderY-y)+1}});
            endTimes[borderY][borderX+1].push_back(globalTime);
            starts[y+(y-borderY)][x-(borderX-x)].push_back({globalTime,{x,r*r-(borderY-y)*(borderY-y)+1}});
            endTimes[y+(y-borderY)][borderX+1].push_back(globalTime);
        }
    }

    vector<vector<int>> answer(n, vector<int>(m, 0));
    for(int y = 0; y < n; y++){
        map<int,RowQuake> current; // all the circles currently active. this is kinda like a set, but a map works because all the times are unique
        for(int x = 0; x < m; x++){
            for(auto& start : starts[y][x]){
                current[start.time] = start.rowQuake;
            }
            for(auto& endTime : endTimes[y][x]){
                current.erase(endTime);
            }
            if(current.size()){
                RowQuake& rq = current.rbegin()->second;
                answer[y][x] = rq.centerShock - (x-rq.centerX)*(x-rq.centerX);
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