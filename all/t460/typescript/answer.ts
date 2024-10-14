function matrixVectorMultiplication(matrix: number[][], vector: number[]): number[] {
    /**
     * Multiplies a matrix by a vector and returns the resulting vector.
     *
     * @param {number[][]} matrix - A 2D array representing the matrix.
     * @param {number[]} vector - A 1D array representing the vector.
     * @returns {number[]} The resulting vector after multiplication.
     *
     * @throws {Error} If the dimensions of the matrix and vector are not compatible for multiplication.
     */

    // Check if the dimensions are compatible
    if (matrix[0].length !== vector.length) {
        throw new Error('The dimensions of the matrix and vector are not compatible for multiplication.');
    }

    let result = [];

    // Perform multiplication
    for(let i = 0; i < matrix.length; i++) {
        let sum = 0;
        for(let j = 0; j < vector.length; j++) {
            sum += matrix[i][j] * vector[j];
        }
        result.push(sum);
    }

    return result;
}