/**
 * Applies a shear transformation to a 2D matrix along the x-axis.
 *
 * @param {Array<Array<number>>} matrix - A 2D array representing the original matrix.
 * @param {number} shearFactor - The factor by which the matrix is sheared along the x-axis.
 * @returns {Array<Array<number>>} The sheared matrix.
 */
function applyShearX(matrix, shearFactor) {
    const rows = matrix.length;
    const cols = matrix[0].length;

    // Create a new matrix with the same dimensions
    const shearedMatrix = Array.from({ length: rows }, () => Array(cols).fill(0));

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            const newX = j + shearFactor * i;
            if (newX >= 0 && newX < cols) {
                shearedMatrix[i][newX] = matrix[i][j];
            }
        }
    }

    return shearedMatrix;
}
const assert = require('assert');


describe('TestShearTransformation', () => {
    it('test_identity_shear', () => {
        // Test with zero shear factor which should return the original matrix unchanged.
        const matrix = [[1, 2], [3, 4]];
        const shearFactor = 0;
        const expectedOutput = [[1, 2], [3, 4]];
        const result = applyShearX(matrix, shearFactor);
        assert.deepStrictEqual(result, expectedOutput, 'The matrix should remain unchanged with zero shear factor.');
    });

    it('test_positive_shear', () => {
        // Test with a positive shear factor.
        const matrix = [[1, 2], [3, 4]];
        const shearFactor = 1;
        const expectedOutput = [[1, 3], [3, 7]];
        const result = applyShearX(matrix, shearFactor);
        assert.deepStrictEqual(result, expectedOutput, 'The matrix should be correctly sheared.');
    });

    it('test_negative_shear', () => {
        // Test with a negative shear factor.
        const matrix = [[1, 2], [3, 4]];
        const shearFactor = -1;
        const expectedOutput = [[1, 1], [3, 1]];
        const result = applyShearX(matrix, shearFactor);
        assert.deepStrictEqual(result, expectedOutput, 'The matrix should be correctly sheared negatively.');
    });

    it('test_high_shear_factor', () => {
        // Test with a high shear factor to see how the matrix adapts to extreme transformations.
        const matrix = [[1, 1], [1, 1]];
        const shearFactor = 10;
        const expectedOutput = [[1, 11], [1, 11]];
        const result = applyShearX(matrix, shearFactor);
        assert.deepStrictEqual(result, expectedOutput, 'The matrix should be correctly sheared with a high shear factor.');
    });
});
