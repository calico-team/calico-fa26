#include <iostream>
#include <vector>
using namespace std;

/**
 * Output whether all of the requests can be fulfilled.
 *
 * N: Number of smoke requests
 * R: Number of seconds needed for a smoke charge to recharge
 * A: List of timestamps where smokes are requested
 */
string solve(int N, int R, vector<int> A) {
	int currCharges = 2;
	int cooldown = R;
	int idx = 0;
	for (int t = 0; t <= A[N - 1]; t++) {
		if (currCharges == 2) {
			cooldown = R;
		}
		else {
			cooldown--;
			if (cooldown == 0) {
				cooldown = R;
				currCharges++;
			}
			if (A[idx] == t) {
				if (currCharges == 0) {
					return "NO";
				}
				else {
					currCharges--;
					idx++;
				}
			}
		}
	}
	return "YES";
}

int main() {
	int T; cin >> T;
	while (T--) {
		int N, R; cin >> N >> R;
		vector<int> A(N);
		for (int i = 0; i < N; i++) {
			cin >> A[i];
		}

		cout << solve(N, R, A) << "\n";
	}
}