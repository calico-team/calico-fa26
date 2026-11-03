#include <iostream>
#include <vector>
#include <map>
using namespace std;

struct Poi{
    int time;
    char c;
    bool isStart; // if false, then it's an end
}; // point of interest (of course, you could implement this without a struct but just using four of vector<vector<vector<>>>)

void solve(){
    int n, m, q;
    cin>>n>>m>>q;
    bool swapDimensions = (n > m);
    if(swapDimensions){
        swap(n, m);
    }
    vector<vector<vector<Poi>>> pois(n,vector<vector<Poi>>(m+1)); // a 2D grid of lists of points of interest (each row is 1 longer than length m because the ending Pois are exclusive)

    for(int globalTime = 0; globalTime<q; globalTime++){
        int x, y, r;
        char c;
        cin>>x>>y>>c>>r;
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
            pois[borderY][x-(borderX-x)].push_back({globalTime,c,true});
            pois[borderY][borderX+1].push_back({globalTime,c,false});
            pois[y+(y-borderY)][x-(borderX-x)].push_back({globalTime,c,true});
            pois[y+(y-borderY)][borderX+1].push_back({globalTime,c,false});
        }
    }

    vector<vector<char>> answer(n, vector<char>(m, '.'));
    for(int y = 0; y < n; y++){
        map<int,char> current; // all the circles currently active. this is kinda like a set, but a map works because all the times are unique
        for(int x = 0; x < m; x++){
            for(auto& poi : pois[y][x]){
                if(poi.isStart){
                    current[poi.time] = poi.c;
                }
                else{
                    current.erase(poi.time);
                }
            }
            if(current.size()){
                answer[y][x] = current.rbegin()->second;
            }
        }
    }
    
    if(swapDimensions){
        for(int x = 0; x < m; x++){
            for(int y = 0; y < n; y++){
                cout<<answer[y][x];
            }
            cout<<'\n';
        }
    }
    else{
        for(int y = 0; y < n; y++){
            for(int x = 0; x < m; x++){
                cout<<answer[y][x];
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