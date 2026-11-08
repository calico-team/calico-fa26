#include <string>
#include <iostream>
#include <vector>
using namespace std;

/*
 * Reads a single string from standard input.
 */
string read_string() {
    string s; cin >> s;
    return s;
}

/*
 * Prints a guess to standard output and flushes the output stream buffer.
 */
void print_guess(string guess) {
    cout << guess << endl;
}

/*
 * Print a sequence of guesses until you guess the answer string.
 * You may use the read_string() and print_guess() helper functions defined above.
 *
 * N: Length of the string
 * K: Number of different -ities
 * A: List containing the different -ities
 */
void solve(int N, int K, vector<char>& A) {
    string guess(N, '_');
    for (int i = 0; i < K; i++) {
        for (int j = 0; j < N; j++) {
            if (guess[j] == '_') {
                guess[j] = A[i];
            }
        }
        
        print_guess(guess);
        guess = read_string();
        if (guess == "CORRECT") {
            break;
        }
    }
}

int main() {
    int T;
    cin >> T;
    
    for (int i = 0; i < T; i++) {
        int N, K;
        cin >> N >> K;

        vector<char> A(K);
        for (int j = 0; j < K; j++) {
            cin >> A[j];
        }

        solve(N, K, A);
    }

    return 0;
}