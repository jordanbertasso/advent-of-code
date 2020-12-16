#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    vector<int> ids;
    string s;

    while(getline(cin, s)) {
        for (int i = 0; i < s.size(); i++) {
            switch (s[i])
            {
            case 'F':
                s[i] = '0';
                break;
            case 'B':
                s[i] = '1';
                break;
            case 'L':
                s[i] = '0';
                break;
            case 'R':
                s[i] = '1';
                break;
            default:
                break;
            }
        }

        ids.push_back(stoi(s, 0, 2));
    }

    int max = 0;
    for (auto x : ids) {
        if (x > max) {
            max = x;
        }
    }

    cout << max << endl;

    sort(ids.begin(), ids.end());

    for (int i = 1; i < ids.size(); i++) {
        if (ids[i] - ids[i-1] == 2 ) {
            cout << ids[i] - 1 << endl;
        }
    }

    return 0;
}