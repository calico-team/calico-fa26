#include <iostream>
#include <vector>
using namespace std;

void solve(){
    int n, m, q;
    cin>>n>>m>>q;
    bool swapDimensions = (n > m); // we will swap things such that n <= m and therefore n <= sqrt(10^5)
    if(swapDimensions){
        swap(n, m);
    }
    vector<vector<int>> answer(n, vector<int>(m, 0));
    vector<vector<int>> next(n, vector<int>(m)); // x position of nearest unmodified tile to the right, or m if none exist
    for(int y = 0; y<n; y++){
        for(int x = 0; x<m; x++){
            next[y][x] = x; // initially, each tile's nearest is itself
        }
    }
    vector<int> xs, ys, rs;
    for(int i = 0; i<q; i++){
        int y, x, r;
        cin>>y>>x>>r;
        if(swapDimensions){
            swap(x, y);
        }
        xs.push_back(x);
        ys.push_back(y);
        rs.push_back(r);
    }
    vector<int> toUpdate;
    for(int i = q-1; i>=0; i--){
        int x = xs[i], y = ys[i], r = rs[i];
        // go through first quadrant of the circle (go top down, see how far right you have to mark the ends)
        int borderX = x;
        for(int borderY = y - r; borderY <= y + r; borderY++){ // we'll double paint the horizontal diameter but that's fine (the map will actually forget about that anyway)
            // these while loops could just be replaced with square root math
            while((borderX-x)*(borderX-x) + (borderY-y)*(borderY-y) <= r*r){
                borderX++;
            }
            while((borderX-x)*(borderX-x) + (borderY-y)*(borderY-y) > r*r){ 
                borderX--;
            }
            // borderX is now as far right as possible while still being in/on the circle
            
            int explorerX = x-(borderX-x);
            toUpdate.clear();
            while(explorerX <= borderX){
                toUpdate.push_back(explorerX);
                if(answer[borderY][explorerX]==0){
                    answer[borderY][explorerX] = r*r - (explorerX-x)*(explorerX-x) - (borderY-y)*(borderY-y) + 1;
                    explorerX += 1;
                }
                else{
                    explorerX = next[borderY][explorerX];
                }
            }
            for(int updateX : toUpdate){
                next[borderY][updateX] = explorerX;
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