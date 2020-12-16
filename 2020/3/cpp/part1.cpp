#include <iostream>

using namespace std;

int main() {
    int x = 0;
    int trees = 0;
    string s;

    while (getline(cin, s)) {
        if (s[x] == '#') {
            trees++;
        }

        x = (x + 3)%s.size();
    }

    cout << trees << endl;
}