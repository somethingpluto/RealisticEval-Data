#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>

// Function to compare two floating-point numbers within a relative and absolute tolerance
bool isclose(double a, double b, double rtol, double atol) {
    return std::abs(a - b) <= std::max(rtol * std::max(std::abs(a), std::abs(b)), atol);
}

// Function to compare two sets of floats for equality within a relative and absolute tolerance
bool are_sets_equal(const std::set<double>& set1, const std::set<double>& set2, double rtol = 1e-5, double atol = 1e-6) {
    // Convert sets to sorted vectors for comparison
    std::vector<double> list1(set1.begin(), set1.end());
    std::vector<double> list2(set2.begin(), set2.end());

    // Check if the lengths of both sets are the same
    if (list1.size() != list2.size()) {
        return false;
    }

    // Compare each element in the two sorted vectors
    for (size_t i = 0; i < list1.size(); ++i) {
        if (!isclose(list1[i], list2[i], rtol, atol)) {
            return false;
        }
    }

    return true;
}