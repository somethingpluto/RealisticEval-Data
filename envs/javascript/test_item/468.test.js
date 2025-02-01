const math = require('mathjs');

/**
 * Given a 3x3 matrix, return the corresponding translation vector.
 *
 * @param {Array<Array<number>>} matrix - A 3x3 affine transformation matrix.
 * @returns {Array<number>} A 2-element array containing the translation components (translation_x, translation_y).
 */
function getTranslation(matrix) {
  // Check if the input matrix is a 3x3 matrix
  if (!Array.isArray(matrix) || matrix.length !== 3 || !matrix.every(row => Array.isArray(row) && row.length === 3)) {
    throw new Error('Input must be a 3x3 matrix');
  }

  // Extract the translation components from the matrix
  const translationX = matrix[2][0];
  const translationY = matrix[2][1];

  // Return the translation vector
  return [translationX, translationY];
}
const math = require('mathjs');

describe('TestGetTranslationFunction', () => {
    describe('test_identity_matrix', () => {
        it('should return the correct translation for the identity matrix', () => {
            const matrix = [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]
            ];
            const expectedTranslation = [0.0, 0.0];
            expect(getTranslation(matrix)).toEqual(expectedTranslation);
        });
    });

    describe('test_translation_matrix', () => {
        it('should return the correct translation for a translation matrix (5 in x, 10 in y)', () => {
            const matrix = [
                [1, 0, 5],
                [0, 1, 10],
                [0, 0, 1]
            ];
            const expectedTranslation = [5.0, 10.0];
            expect(getTranslation(matrix)).toEqual(expectedTranslation);
        });
    });

    describe('test_negative_translation', () => {
        it('should return the correct translation for a translation matrix with negative values', () => {
            const matrix = [
                [1, 0, -3],
                [0, 1, -6],
                [0, 0, 1]
            ];
            const expectedTranslation = [-3.0, -6.0];
            expect(getTranslation(matrix)).toEqual(expectedTranslation);
        });
    });
});
