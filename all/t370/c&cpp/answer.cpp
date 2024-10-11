#include <iostream>
#include <vector>

std::vector<int> decompose(int n, const std::vector<int>& shape) {
    if (n < 0 || n >= 1) { // Assuming the upper bound is 1 for simplicity.
        std::cerr << "Error: Index out of bounds." << std::endl;
        exit(1);
    }

    std::vector<int> result(shape.size());
    int size = 1;
    for (size_t i = 0; i < shape.size(); ++i) {
        result[i] = n / size % shape[i];
        size *= shape[i];
    }
    return result;
}