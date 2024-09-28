#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include <catch2/catch.hpp>
#include <vector>
#include <stdexcept>

using namespace std;

// Function prototype
vector<vector<int>> matrix_multiply(const vector<vector<int>>& matrixA, const vector<vector<int>>& matrixB);

// Define the matrix multiplication function
vector<vector<int>> matrix_multiply(const vector<vector<int>>& matrixA, const vector<vector<int>>& matrixB) {
    if (matrixA.empty() || matrixB.empty() || matrixA[0].empty() || matrixB[0].empty()) {
        return {};
    }

    if (matrixA[0].size() != matrixB.size()) {
        throw invalid_argument("The number of columns in the first matrix must be equal to the number of rows in the second matrix.");
    }

    vector<vector<int>> result(matrixA.size(), vector<int>(matrixB[0].size(), 0));

    for (size_t i = 0; i < matrixA.size(); ++i) {
        for (size_t j = 0; j < matrixB[0].size(); ++j) {
            for (size_t k = 0; k < matrixB.size(); ++k) {
                result[i][j] += matrixA[i][k] * matrixB[k][j];
            }
        }
    }

    return result;
}

// Start of testing with Catch2
TEST_CASE("Testing matrix_multiply function", "[matrix_multiply]") {
    SECTION("Test standard matrices") {
        vector<vector<int>> mat1 = {{1, 2}, {3, 4}};
        vector<vector<int>> mat2 = {{5, 6}, {7, 8}};
        vector<vector<int>> expected = {{19, 22}, {43, 50}};
        REQUIRE(matrix_multiply(mat1, mat2) == expected);
    }

    SECTION("Test empty matrices") {
        vector<vector<int>> mat1 = {};
        vector<vector<int>> mat2 = {};
        vector<vector<int>> expected = {};
        REQUIRE(matrix_multiply(mat1, mat2) == expected);
    }

    SECTION("Test identity matrix") {
        vector<vector<int>> mat1 = {{1, 0}, {0, 1}};
        vector<vector<int>> mat2 = {{5, 6}, {7, 8}};
        vector<vector<int>> expected = {{5, 6}, {7, 8}};
        REQUIRE(matrix_multiply(mat1, mat2) == expected);
    }
}