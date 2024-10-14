function matrixVectorMultiplication(matrix: number[][], vector: number[]): number[] {
    /**
     * Multiplies a given matrix by a vector using a nested loop approach.
     *
     * Parameters:
     * matrix (number[][]): A 2D array (matrix) of shape (m, n) where m is the number of rows
                             and n is the number of columns.
     * vector (number[]): A 1D array (vector) of shape (n,) that represents a vector
                         compatible for multiplication with the given matrix.
     *
     * Returns:
     * number[]: A 1D array (resulting vector) of shape (m,) representing the product of
                 the matrix and the vector.
     */

    // Check if the number of columns in the matrix matches the length of the vector
    if (matrix[0].length !== vector.length) {
        throw new Error("The number of columns in the matrix must match the length of the vector.");
    }

    const m = matrix.length;
    const n = vector.length;

    // Initialize the resulting vector with zeros
    const result: number[] = new Array(m).fill(0);

    // Perform matrix-vector multiplication using nested loops
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            result[i] += matrix[i][j] * vector[j];
        }
    }

    // Return the resulting vector from the multiplication
    return result;
}
