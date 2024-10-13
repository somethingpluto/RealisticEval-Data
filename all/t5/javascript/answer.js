function matrixMultiply(matrixA, matrixB) {
    /**
     * Implementing matrix multiplication
     * @param {Array<Array<number>>} matrixA - matrix A
     * @param {Array<Array<number>>} matrixB - matrix B
     * @returns {Array<Array<number>>} matrixA * matrixB multiplication result
     */

    // Check if either matrix is empty or has no elements
    if (!matrixA || !matrixB || !matrixA[0] || !matrixB[0]) {
        return [];
    }

    // Ensure matrix dimensions are compatible for multiplication
    if (matrixA[0].length !== matrixB.length) {
        throw new Error(
            "The number of columns in the first matrix must be equal to the number of rows in the second matrix."
        );

    }

    // Initialize the result matrix with zeros
    const result = Array.from({ length: matrixA.length }, () => 
        Array.from({ length: matrixB[0].length }, () => 0)
    );

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