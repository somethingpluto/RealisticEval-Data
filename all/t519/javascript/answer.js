function transposeMatrix(matrix) {
    /**
     * Transpose a given matrix (2D array).
     *
     * @param {Array<Array<number>>} matrix - The input 2D array to be transposed.
     * @returns {Array<Array<number>>} The transposed 2D array.
     */
    // Check if the matrix is empty
    if (!matrix || !matrix[0]) {
        return [];
    }

    const numRows = matrix.length;
    const numCols = matrix[0].length;

    // Initialize the transposed matrix with the correct dimensions
    const transposed = Array.from({ length: numCols }, () => Array(numRows).fill(0));

    for (let i = 0; i < numRows; i++) {
        for (let j = 0; j < numCols; j++) {
            transposed[j][i] = matrix[i][j];
        }
    }

    return transposed;
}