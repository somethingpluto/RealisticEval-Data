#include <iostream>
#include <vector>

// Function to perform matrix-vector multiplication
std::vector<double> matrix_vector_multiplication(const std::vector<std::vector<double>>& matrix, const std::vector<double>& vector) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    int vecSize = vector.size();

    // Check if the dimensions are compatible
    if (cols != vecSize) {
        throw std::invalid_argument("Matrix and vector dimensions are incompatible.");
    }

    std::vector<double> result(rows);

    for (int i = 0; i < rows; ++i) {
        double sum = 0.0;
        for (int j = 0; j < cols; ++j) {
            sum += matrix[i][j] * vector[j];
        }
        result[i] = sum;
    }

    return result;
}
