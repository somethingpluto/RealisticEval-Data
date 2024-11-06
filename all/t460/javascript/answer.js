function matrixVectorMultiplication(matrix, vector) {
    if (matrix[0].length !== vector.length) {
        throw new Error("Matrix and vector dimensions are not compatible for multiplication");
    }
    const result = new Array(matrix.length).fill(0.0);
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < vector.length; j++) {
            result[i] += matrix[i][j] * vector[j];
        }
    }

    return result;
}