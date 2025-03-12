/**
 * Multiplies a matrix by a vector and returns the resulting vector.
 *
 * @param {number[][]} matrix - A 2D array representing the matrix.
 * @param {number[]} vector - A 1D array representing the vector.
 * @returns {number[]} The resulting vector after multiplication.
 * @throws {Error} If the dimensions of the matrix and vector are not compatible for multiplication.
 */
function matrixVectorMultiplication(matrix, vector) {
    // Check if the number of columns in the matrix matches the length of the vector
    const numRows = matrix.length;
    const numCols = matrix[0].length;

    if (numCols !== vector.length) {
        throw new Error("Matrix and vector dimensions are not compatible for multiplication.");
    }

    // Initialize the resulting vector with zeros
    const result = new Array(numRows).fill(0);

    // Perform the matrix-vector multiplication
    for (let i = 0; i < numRows; i++) {
        for (let j = 0; j < numCols; j++) {
            result[i] += matrix[i][j] * vector[j];
        }
    }

    return result;
}
describe('TestMatrixVectorMultiplication', () => {
    it('test_non_square_matrix', () => {
        // Test case for a non-square matrix and a compatible vector.
        const matrix = [[1, 2], [3, 4], [5, 6]];
        const vector = [2, 3];
        const expectedResult = [8.0, 18.0, 28.0];
        expect(matrixVectorMultiplication(matrix, vector)).toEqual(expectedResult);
    });

    it('test_zero_vector', () => {
        // Test case for a matrix and a zero vector.
        const matrix = [[1, 2, 3], [4, 5, 6]];
        const vector = [0, 0, 0];
        const expectedResult = [0.0, 0.0];
        expect(matrixVectorMultiplication(matrix, vector)).toEqual(expectedResult);
    });

    it('test_single_element', () => {
        // Test case for a single element matrix and vector.
        const matrix = [[5]];
        const vector = [3];
        const expectedResult = [15.0];
        expect(matrixVectorMultiplication(matrix, vector)).toEqual(expectedResult);
    });

    it('test_single_element_matrix_and_vector', () => {
        // Test case with a single element in the matrix and vector.
        const matrix = [[3]];
        const vector = [4];
        const expected = [12];
        expect(matrixVectorMultiplication(matrix, vector)).toEqual(expected);
    });

    it('test_compatible_sizes', () => {
        // Test case with compatible sizes but different dimensions.
        const matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
        const vector = [1, 1, 1];
        const expected = [6, 15, 24];
        expect(matrixVectorMultiplication(matrix, vector)).toEqual(expected);
    });
});
