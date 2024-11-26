#include <iostream>
#include <vector>
#include <stdexcept>

// Function to perform matrix-vector multiplication
std::vector<float> matrix_vector_multiplication(const std::vector<std::vector<float>>& matrix, const std::vector<float>& vector) {
    // Ensure matrix dimensions are compatible with vector length
    if (matrix[0].size() != vector.size()) {
        throw std::invalid_argument("Matrix and vector dimensions are not compatible for multiplication");
    }

    // Initialize the result vector with zeros
    std::vector<float> result(matrix.size(), 0.0f);

    // Perform the matrix-vector multiplication
    for (size_t i = 0; i < matrix.size(); ++i) {
        for (size_t j = 0; j < vector.size(); ++j) {
            result[i] += matrix[i][j] * vector[j];
        }
    }

    return result;
}