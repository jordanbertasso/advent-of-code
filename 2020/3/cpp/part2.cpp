#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> xs = {1, 3, 5, 7, 1};
    vector<int> ys = {1, 1, 1, 1, 2};
    vector<string> map;

    string s;
    while (getline(cin, s))
    {
        map.push_back(s);
    }

    long long res = 1;
    for (int i = 0; i < xs.size(); i++)
    {
        int x = 0;
        int y = 0;
        int trees = 0;

        while (y < map.size())
        {
            if (map[y][x] == '#')
            {
                trees++;
            }

            x = (x + xs[i]) % map[y].size();
            y = (y + ys[i]);
        }

        res *= trees;
    }

    cout << res << endl;
}