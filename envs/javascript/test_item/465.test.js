const math = require('mathjs');

/**
 * Multiplies a given matrix by a vector using mathjs's multiply function.
 * 
 * @param {Array<Array<number>>} matrix - A 2D array (matrix) of shape (m, n) where m is the number of rows
 *                                        and n is the number of columns.
 * @param {Array<number>} vector - A 1D array (vector) of shape (n,) that represents a vector
 *                                 compatible for multiplication with the given matrix.
 * @returns {Array<number>} - A 1D array (resulting vector) of shape (m,) representing the product of
 *                            the matrix and the vector.
 */
function matrixVectorMultiplication(matrix, vector) {
    // Convert the matrix and vector to mathjs matrices
    const mathMatrix = math.matrix(matrix);
    const mathVector = math.matrix(vector);

    // Perform the multiplication
    const result = math.multiply(mathMatrix, mathVector);

    // Convert the result back to a 1D array
    return result.toArray();
}
const math = require('mathjs');

describe('TestMatrixVectorMultiplication', () => {
    it('test_case_1', () => {
        // Test with a simple 2x2 matrix and a 2-element vector
        const matrix = [[1, 2], [3, 4]];
        const vector = [5, 6];
        const expected_result = [17, 39];  // [1*5 + 2*6, 3*5 + 4*6]
        expect(matrixVectorMultiplication(matrix, vector)).toEqual(expected_result);
    });

    it('test_case_2', () => {
        // Test with a 3x3 matrix and a 3-element vector
        const matrix = [[1, 0, 2], [0, 1, 2], [1, 1, 0]];
        const vector = [3, 4, 5];
        const expected_result = [13, 14, 7];  // [1*3 + 0*4 + 2*5, 0*3 + 1*4 + 2*5, 1*3 + 1*4 + 0*5]
        expect(matrixVectorMultiplication(matrix, vector)).toEqual(expected_result);
    });

    it('test_case_3', () => {
        // Test with a zero matrix and a vector
        const matrix = [[0, 0], [0, 0]];
        const vector = [1, 1];
        const expected_result = [0, 0];  // Zero matrix multiplied by any vector yields zero
        expect(matrixVectorMultiplication(matrix, vector)).toEqual(expected_result);
    });

    it('test_case_4', () => {
        // Test with a matrix having negative values
        const matrix = [[-1, -2], [-3, -4]];
        const vector = [1, 1];
        const expected_result = [-3, -7];  // [-1*1 + -2*1, -3*1 + -4*1]
        expect(matrixVectorMultiplication(matrix, vector)).toEqual(expected_result);
    });

    it('test_case_5', () => {
        // Test with non-square matrix (2x3) and a compatible vector (3-element)
        const matrix = [[1, 2, 3], [4, 5, 6]];
        const vector = [1, 0, 1];
        const expected_result = [4, 10];  // [1*1 + 2*0 + 3*1, 4*1 + 5*0 + 6*1]
        expect(matrixVectorMultiplication(matrix, vector)).toEqual(expected_result);
    });
});
