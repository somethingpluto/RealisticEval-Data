
/**
 * Multiplies a given matrix by a vector.
 *
 * @param matrix The input matrix represented as a vector of vectors.
 * @param vector The input vector represented as a vector.
 * @return The resulting vector after multiplying the matrix and the vector.
 */
std::vector<double> matrixVectorMultiplication(const std::vector<std::vector<double>>& matrix, const std::vector<double>& vector) {
    // Check if the dimensions are compatible for multiplication
    size_t numRows = matrix.size();
    size_t numCols = matrix[0].size();
    size_t vecSize = vector.size();

    if (numCols != vecSize) {
        throw std::invalid_argument("Matrix and vector dimensions do not match.");
    }

    // Initialize the resulting vector with zeros
    std::vector<double> result(numRows, 0);

    // Perform matrix-vector multiplication
    for (size_t i = 0; i < numRows; ++i) {
        for (size_t j = 0; j < numCols; ++j) {
            result[i] += matrix[i][j] * vector[j];
        }
    }

    // Return the resulting vector
    return result;
}