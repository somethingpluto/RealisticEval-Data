#include <iostream>
#include <vector>
#include <stdexcept>

// Function to multiply two matrices
std::vector<std::vector<int>> matrix_multiply(const std::vector<std::vector<int>>& matrixA, const std::vector<std::vector<int>>& matrixB) {
    // Check if either matrix is empty or if the dimensions are incompatible
    if (matrixA.empty() || matrixB.empty() || matrixA[0].empty() || matrixB[0].empty()) {
        return {};
    }
    if (matrixA[0].size() != matrixB.size()) {
        throw std::invalid_argument("The number of columns in the first matrix must be equal to the number of rows in the second matrix.");
    }

    // Initialize the result matrix with zeros
    std::vector<std::vector<int>> result(matrixA.size(), std::vector<int>(matrixB[0].size(), 0));

    // Perform matrix multiplication
    for (size_t i = 0; i < matrixA.size(); ++i) {
        for (size_t j = 0; j < matrixB[0].size(); ++j) {
            for (size_t k = 0; k < matrixB.size(); ++k) {
                result[i][j] += matrixA[i][k] * matrixB[k][j];
            }
        }
    }

    return result;
}