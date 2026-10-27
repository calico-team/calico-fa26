#include <iostream>
#include <string>
#include <vector>
using namespace std;

/**
 * Send one guess to the judge and return the judge's reply.
 *
 * GUESS: a string of length N, one character per position
 * Returns: the judge's reply for this guess: either the string
 *          "CORRECT", or a string of length N where position i shows
 *          the true character if GUESS[i] was correct and '_' otherwise.
 */
string submit(string GUESS) {
    cout << GUESS << '\n' << flush;
    string reply;
    cin >> reply;
    return reply;
}

/**
 * Guess the hidden string of length N.
 *
 * N: the length of the hidden string
 * K: the number of allowed characters
 * A: the list of the K allowed characters
 * The hidden string must be guessed using submit(); use no more than
 * 2*N guesses.
 */
void solve(int N, int K, vector<string>& A) {
    // YOUR CODE HERE
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int N, K;
        cin >> N >> K;
        vector<string> A(K);
        for (int j = 0; j < K; j++) {
            cin >> A[j];
        }
        solve(N, K, A);
    }
}
