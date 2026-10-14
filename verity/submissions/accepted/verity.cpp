#include <string>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int stringSize, characters;
        cin >> stringSize >> characters;
        vector<char> character;
        for (int i = 0; i < characters; i++) {
            char chara;
            cin >> chara;
            character.push_back(chara);
        }
        string stri(stringSize, '.');
        for (int i = 0; i < character.size() - 1; i++) {
            for (int a = 0; a < stringSize; a++) {
                if (stri[a] == '.') {
                    stri[a] = character[i];
                }
            }
            cout << "? " << stri << endl;
            cin >> stri;
        }
        for (int i = 0; i < stringSize; i++) {
            if (stri[i] == '.') {
                stri[i] = character[character.size() - 1];
            }
        }
        cout << "! " << stri << endl;
    }
}