import { NDArray } from 'ndarray';

/**
 * Multiplies a given matrix by a vector using NumPy's dot product.
 *
 * @param matrix - A 2D array (matrix) of shape (m, n) where m is the number of rows
 *                 and n is the number of columns.
 * @param vector - A 1D array (vector) of shape (n,) that represents a vector
 *                 compatible for multiplication with the given matrix.
 * @returns A 1D array (resulting vector) of shape (m,) representing the product of
 *          the matrix and the vector.
 */
function matrixVectorMultiplication(matrix: NDArray, vector: NDArray): NDArray {
    // Perform matrix-vector multiplication using the dot product function.
    const result = matrix.mul(vector);

    // Return the resulting vector from the multiplication.
    return result;
}