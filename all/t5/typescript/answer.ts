/**
 * Implementing matrix multiplication.
 * @param matrixA - matrix A
 * @param matrixB - matrix B
 * @returns The result of multiplying matrixA by matrixB
 */
function matrixMultiply(matrixA: number[][], matrixB: number[][]): number[][] {

    // Check if either matrix is empty or has no elements
    if (!matrixA.length || !matrixB.length || !matrixA[0].length || !matrixB[0].length) {
        return [];
    }

    // Ensure matrix dimensions are compatible for multiplication
    if (matrixA[0].length !== matrixB.length) {
        throw new Error(
            "The number of columns in the first matrix must be equal to the number of rows in the second matrix."
        );
    }

    // Initialize the result matrix with zeros
    const result: number[][] = Array.from({ length: matrixA.length }, () =>
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