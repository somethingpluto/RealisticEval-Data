#include <iostream>
#include <string>
#include <vector>
#include <numeric>
#include <algorithm>

void greet(const std::string& name) {
    if (name.empty() || std::all_of(name.begin(), name.end(), isspace)) {
        std::cout << "Hello, Guest!" << std::endl;
    } else {
        std::cout << "Hello, " << name << "!" << std::endl;
    }
}

int sum(const std::vector<int>& arr) {
    if (!std::all_of(arr.begin(), arr.end(), [](int n) { return std::is_integral<int>::value; })) {
        throw std::invalid_argument("Expected an array of numbers");
    }

    return std::accumulate(arr.begin(), arr.end(), 0);
}