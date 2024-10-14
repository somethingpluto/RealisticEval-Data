#include <iostream>
#include <vector>

std::vector<double> matrixVectorMultiplication(const std::vector<std::vector<double>>& matrix, const std::vector<double>& vector) {
    int rows = matrix.size();
    int cols = matrix[0].size();

    // Check if the dimensions are compatible for multiplication
    if (cols != vector.size()) {
        throw std::invalid_argument("Matrix and vector dimensions are not compatible for multiplication.");
    }

    std::vector<double> result(rows, 0.0);

    // Perform matrix-vector multiplication
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            result[i] += matrix[i][j] * vector[j];
        }
    }

    return result;
}

int main() {
    // Example usage
    std::vector<std::vector<double>> matrix = {{1, 2, 3}, {4, 5, 6}};
    std::vector<double> vector = {7, 8, 9};

    try {
        std::vector<double> result = matrixVectorMultiplication(matrix, vector);

        // Print the result
        for (const auto& val : result) {
            std::cout << val << " ";
        }
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}