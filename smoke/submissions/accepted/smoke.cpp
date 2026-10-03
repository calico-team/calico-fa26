#include <iostream>
#include <vector>

using namespace std;

string solve() {
    int n;
    cin>>n;
    vector<int> times(n+1);
    times[0] = 0;

    for(int i = 0; i<n; ++i){
        cin>>times[i+1];
    }

    sort(times.begin(),times.end()); // we can remove this line if we make the input sorted
    
    int wait = 80;
    
    for(int i = 1; i<=n; ++i){
        wait += times[i]-times[i-1];
        wait = min(80, wait);
        
        if(wait >= 40){
            wait -= 40;
        }else{
            return "NO";
        }
    }

    return "YES";
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
       
        cout << solve() << '\n';
    }
}