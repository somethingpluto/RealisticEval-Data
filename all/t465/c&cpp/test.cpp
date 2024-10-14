#include <catch2/catch.hpp>
#include <iostream>
#include <array>

// Define the function that performs matrix-vector multiplication
std::array<double, 3> matrixVectorMultiplication(const std::array<std::array<double, 3>, 2>& matrix, const std::array<double, 3>& vector) {
    // Perform matrix-vector multiplication
    double result[3] = {0};
    for (size_t i = 0; i < 2; ++i) {
        for (size_t j = 0; j < 3; ++j) {
            result[i] += matrix[i][j] * vector[j];
        }
    }

    // Return the resulting vector
    return {result[0], result[1], result[2]};
}

TEST_CASE("Matrix-Vector Multiplication", "[math]") {
    // Test data
    std::array<std::array<double, 3>, 2> matrix = {{{1.0, 2.0, 3.0}, {4.0, 5.0, 6.0}}};
    std::array<double, 3> vector = {1.0, 0.0, -1.0};
    std::array<double, 3> expected_result = {-2.0, 8.0};

    // Call the function under test
    auto result = matrixVectorMultiplication(matrix, vector);

    // Check if the result matches the expected result
    REQUIRE(result == Approx(expected_result));
}