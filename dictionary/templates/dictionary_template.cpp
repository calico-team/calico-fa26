#include <iostream>
#include <vector>
using namespace std;

/**
 * Return an array of N integers, the i-th of which
 * represents Big Ben's maximum happiness if he 
 * starts by trying to define word i.
 *
 * N: the number of words in the dictionary
 * A: the value associated with the happiness of each word
 * B: the first word in the definition of word i
 */ 
vector<int> solve(int N, vector<int> A, vector<int> B) {
	// YOUR CODE HERE
	return {};
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int T; cin >> T;
	while (T--) {
		int N; cin >> N;
        vector<int> A(N), B(N);
        for (int& i : A) cin >> i;
        for (int& i : B) cin >> i;
        vector<int> ans = solve(N, A, B);
        for (int& i : ans) cout << i << ' ';
        cout << '\n';
	}
	return 0;
}

