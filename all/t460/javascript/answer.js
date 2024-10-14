function matrixVectorMultiplication(matrix, vector) {
    // Check if the dimensions of the matrix and vector are compatible for multiplication
    if (matrix[0].length !== vector.length) {
        throw new Error('The dimensions of the matrix and vector are not compatible for multiplication.');
    }

    let result = [];

    // Perform matrix-vector multiplication
    for (let i = 0; i < matrix.length; i++) {
        let sum = 0;
        for (let j = 0; j < vector.length; j++) {
            sum += matrix[i][j] * vector[j];
        }
        result.push(sum);
    }

    return result;
}