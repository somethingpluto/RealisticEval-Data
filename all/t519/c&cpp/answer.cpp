#include <vector>
#include <iostream>

// Function to transpose a given matrix (2D vector).
std::vector<std::vector<int>> transpose_matrix(const std::vector<std::vector<int>>& matrix) {
    // Check if the matrix is empty
    if (matrix.empty() || matrix[0].empty()) {
        return {};
    }

    size_t num_rows = matrix.size();
    size_t num_cols = matrix[0].size();

    // Initialize the transposed matrix with the correct dimensions
    std::vector<std::vector<int>> transposed(num_cols, std::vector<int>(num_rows, 0));

    for (size_t i = 0; i < num_rows; ++i) {
        for (size_t j = 0; j < num_cols; ++j) {
            transposed[j][i] = matrix[i][j];
        }
    }

    return transposed;
}
