function transposeMatrix(matrix: number[][]): number[][] {
    /**
     * Transpose a given matrix (2D array).
     *
     * @param matrix - The input 2D array to be transposed.
     * @returns The transposed 2D array.
     */
    // Check if the matrix is empty
    if (!matrix.length || !matrix[0].length) {
        return [];
    }

    const numRows = matrix.length;
    const numCols = matrix[0].length;

    // Initialize the transposed matrix with the correct dimensions
    const transposed: number[][] = Array.from({ length: numCols }, () => Array(numRows).fill(0));

    for (let i = 0; i < numRows; i++) {
        for (let j = 0; j < numCols; j++) {
            transposed[j][i] = matrix[i][j];
        }
    }

    return transposed;
}