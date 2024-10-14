#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file

#include "catch.hpp"
#include <vector>
#include <cmath>

// Function to compare two matrices for equality within a tolerance
bool matrices_equal(const std::vector<std::vector<double>>& m1, const std::vector<std::vector<double>>& m2, double tolerance = 1e-6) {
    if (m1.size() != m2.size() || m1[0].size() != m2[0].size()) {
        return false;
    }
    for (size_t i = 0; i < m1.size(); ++i) {
        for (size_t j = 0; j < m1[i].size(); ++j) {
            if (std::abs(m1[i][j] - m2[i][j]) > tolerance) {
                return false;
            }
        }
    }
    return true;
}

// Test case using Catch2
TEST_CASE("Apply Shear X Transformation", "[shear]") {
    // Define a sample matrix
    std::vector<std::vector<double>> matrix = {
        {1.0, 2.0, 3.0},
        {4.0, 5.0, 6.0},
        {7.0, 8.0, 9.0}
    };

    // Define a shear factor
    double shear_factor = 0.5;

    // Expected result after applying shear transformation
    std::vector<std::vector<double>> expected_result = {
        {1.0, 1.5, 2.5},
        {4.0, 4.5, 5.5},
        {7.0, 7.5, 8.5}
    };

    // Apply the shear transformation
    std::vector<std::vector<double>> result = apply_shear_x(matrix, shear_factor);

    // Check if the result matches the expected result
    REQUIRE(matrices_equal(result, expected_result));
}
