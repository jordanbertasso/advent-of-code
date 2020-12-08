#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec;
    int x;

    while (std::cin >> x) {
        vec.push_back(x);
    }

    for (unsigned int i = 0; i < vec.size(); i++) {
        for (unsigned int j = 0; j < vec.size()-1; j++) {
            for (unsigned int k = 0; k < vec.size()-2; k++) {
                if (vec[i] + vec[j] + vec[k] == 2020) {
                    std::cout << vec[i]*vec[j]*vec[k] << std::endl;
                    return 0;
                }
            }
        }
    }

    return 0;
}
