#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {

    vector<string> vec;

    // 1-3 l: llll

    string pass, s;
    int min, max, occ, res;
    char junk, letter;
    while (cin) {
        cin >> min >> junk >> max >> letter >> junk >> pass;

        occ = count(pass.begin(), pass.end(), letter);

        if (min <= occ && occ <= max) {
            res++;
        }
    }

    std::cout << res << std::endl;

    return 0;
}
