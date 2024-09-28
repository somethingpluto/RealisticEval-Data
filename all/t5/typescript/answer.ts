function matrixMultiply(matrixA: number[][], matrixB: number[][]): number[][] {
    /**
     * Implementing matrix multiplication
     * Args:
     *     matrixA (): matrix A
     *     matrixB (): matrix B
     * 
     * Returns: matrixA matrixB multiplication result
     * 
     */
    if (!matrixA.length || !matrixB.length || !matrixA[0].length || !matrixB[0].length) {
        return [];
    }
    // Ensure matrix dimensions are compatible for multiplication
    if (matrixA[0].length !== matrixB.length) {
        throw new Error("The number of columns in the first matrix must be equal to the number of rows in the second matrix.");
    }

    // Initialize the result matrix with zeros
    const result: number[][] = new Array(matrixA.length).fill(0).map(() => new Array(matrixB[0].length).fill(0));

    // Perform matrix multiplication
    for (let i = 0; i < matrixA.length; i++) {
        for (let j = 0; j < matrixB[0].length; j++) {
            for (let k = 0; k < matrixB.length; k++) {
                result[i][j] += matrixA[i][k] * matrixB[k][j];
            }
        }
    }

    return result;
}