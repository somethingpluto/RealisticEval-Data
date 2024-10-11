/**
 * Computes the n-th power of a matrix using the fast exponentiation method.
 *
 * @param matrix A square matrix to be exponentiated.
 * @param n The exponent to raise the matrix to. Must be a non-negative integer.
 * @return The matrix raised to the power of n.
 * @throw std::invalid_argument if n is negative.
 * @throw std::invalid_argument if matrix is not a square matrix.
 */
std::vector<std::vector<int>> power(const std::vector<std::vector<int>>& matrix, int n);