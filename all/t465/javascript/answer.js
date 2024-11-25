function matrixVectorMultiplication(matrix, vector) {
    if (matrix[0].length !== vector.length) {
        throw new Error("The number of columns in the matrix must match the length of the vector.");
    }

    const m = matrix.length;
    const n = vector.length;

    // Initialize the resulting vector with zeros
    const result = new Array(m).fill(0);

    // Perform matrix-vector multiplication using nested loops
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            result[i] += matrix[i][j] * vector[j];
        }
    }

    // Return the resulting vector from the multiplication
    return result;
}
