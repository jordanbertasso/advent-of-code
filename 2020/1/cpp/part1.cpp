#include <vector>
#include <iostream>

int main() {
	std::vector<int> vec;
	int x;

	while (std::cin >> x) {
		vec.push_back(x);
	}

	for (unsigned int i = 0; i < vec.size(); i++) {
		for (unsigned int j = i+1; j < vec.size()-1; j++) {
			if (vec[i] + vec[j] == 2020) {
				std::cout << vec[i] * vec[j] << std::endl;
				return 0;
			}
		}
	}

	return 0;
}
