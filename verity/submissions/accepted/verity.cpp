#include <string>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N, K;
        cin >> N >> K;
        vector<char> A(N);
        for (int i = 0; i < K; i++) {
            cin >> A[i];
        }

        string guess(N, '_');
        for (int i = 0; i < K; i++) {
            for (int j = 0; j < N; j++) {
                if (guess[j] == '_') {
                    guess[j] = A[i];
                }
            }
            cout << guess << endl;
            cin >> guess;
            if (guess == "CORRECT") {
                break;
            }
        }
    }
}