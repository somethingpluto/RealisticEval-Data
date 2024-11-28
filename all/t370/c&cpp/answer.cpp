#include <iostream>
#include <vector>
#include <tuple>
#include <stdexcept>

// Function to decompose a flat index into a multidimensional index based on the given shape
std::tuple<int, int, int> decompose(int n, const std::vector<int>& shape) {
    // Calculate the total size of the array
    int size = 1;
    for (int dim : shape) {
        size *= dim;
    }

    // Check if the index is within bounds
    if (n < 0 || n >= size) {
        throw std::out_of_range("Index out of bounds");
    }

    // Decompose the index
    std::vector<int> result;
    for (auto it = shape.rbegin(); it != shape.rend(); ++it) {
        result.push_back(n % *it);
        n /= *it;  // Update n by integer division
    }

    // Reverse the result to match the original shape order and return as tuple
    std::tuple<int, int, int> result_tuple(result.back(), result[1], result.front());
    return result_tuple;
}