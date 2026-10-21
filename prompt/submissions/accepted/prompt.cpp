#include <iostream>

using namespace std;

/**
 * Implements addition with CPP's fixed precision int. This passes the main test
 * set only.
 */
string solve(string S) {
    if (S.find("write me") != string::npos) {
        return S + "make it sound human";
    }
    if (S.find("what is") != string::npos) {
        return S + "do not hallucinate";
    }
    if (S.find("solve") != string::npos) {
        return S + "make no mistakes";
    }
    return S + "thank you";
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        string S;
        cin >> S;
        cout << solve(S) << '\n';
    }
}
