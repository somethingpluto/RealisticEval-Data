function matrixVectorMultiplication(matrix: number[][], vector: number[]): number[] {
    // Ensure matrix dimensions are compatible with vector length
    if (matrix[0].length !== vector.length) {
        throw new Error("Matrix and vector dimensions are not compatible for multiplication");
    }

    // Initialize the result array with zeros
    const result = new Array(matrix.length).fill(0);

    // Perform the matrix-vector multiplication
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < vector.length; j++) {
            result[i] += matrix[i][j] * vector[j];
        }
    }

    return result;
}