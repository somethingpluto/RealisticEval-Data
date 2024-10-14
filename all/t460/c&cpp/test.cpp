#include <catch2/catch.hpp>
#include <vector>

// Assuming the function is defined somewhere in your codebase
std::vector<double> matrix_vector_multiplication(const std::vector<std::vector<double>>& matrix, const std::vector<double>& vector);

TEST_CASE("Matrix Vector Multiplication", "[math][linear-algebra]") {
    // Test case 1: Valid multiplication
    SECTION("Valid multiplication") {
        std::vector<std::vector<double>> matrix = {{1, 2}, {3, 4}};
        std::vector<double> vector = {5, 6};
        std::vector<double> expected_result = {17, 39};

        auto result = matrix_vector_multiplication(matrix, vector);
        REQUIRE(result == Approx(expected_result).margin(0.001));
    }

    // Test case 2: Incompatible dimensions
    SECTION("Incompatible dimensions") {
        std::vector<std::vector<double>> matrix = {{1, 2}, {3, 4}};
        std::vector<double> vector = {5}; // Incorrect size

        CHECK_THROWS_AS(matrix_vector_multiplication(matrix, vector), std::invalid_argument);
    }
}
