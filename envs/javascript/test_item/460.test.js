/**
 * Multiplies a matrix by a vector and returns the resulting vector.
 *
 * @param {number[][]} matrix - A 2D array representing the matrix.
 * @param {number[]} vector - A 1D array representing the vector.
 * @returns {number[]} The resulting vector after multiplication.
 * @throws {Error} If the dimensions of the matrix and vector are not compatible for multiplication.
 */
function matrixVectorMultiplication(matrix, vector) {
    if (matrix[0].length !== vector.length) {
        throw new Error('The dimensions of the matrix and vector are not compatible for multiplication.');
    }

    const result = [];

    for (let i = 0; i < matrix.length; i++) {
        let sum = 0;
        for (let j = 0; j < matrix[i].length; j++) {
            sum += matrix[i][j] * vector[j];
        }
        result.push(sum);
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
