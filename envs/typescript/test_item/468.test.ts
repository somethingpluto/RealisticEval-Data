import * as math from 'mathjs';

/**
 * Given a 3x3 matrix, return the corresponding translation vector.
 *
 * @param matrix - A 3x3 affine transformation matrix.
 * @returns A 2-element array containing the translation components (translation_x, translation_y).
 */
function getTranslation(matrix: number[][]): number[] {
    // Extract the translation components from the last column of the matrix
    const translationX = matrix[0][2];
    const translationY = matrix[1][2];

    // Return the translation vector as a 2-element array
    return [translationX, translationY];
}
describe('TestGetTranslationFunction', () => {
  describe('test_identity_matrix', () => {
      it('should return the correct translation for the identity matrix', () => {
          const matrix: number[][] = [
              [1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]
          ];
          const expectedTranslation: number[] = [0.0, 0.0];
          expect(getTranslation(matrix)).toEqual(expectedTranslation);
      });
  });

  describe('test_translation_matrix', () => {
      it('should return the correct translation for a translation matrix', () => {
          const matrix: number[][] = [
              [1, 0, 5],
              [0, 1, 10],
              [0, 0, 1]
          ];
          const expectedTranslation: number[] = [5.0, 10.0];
          expect(getTranslation(matrix)).toEqual(expectedTranslation);
      });
  });

  describe('test_negative_translation', () => {
      it('should return the correct translation for a translation matrix with negative values', () => {
          const matrix: number[][] = [
              [1, 0, -3],
              [0, 1, -6],
              [0, 0, 1]
          ];
          const expectedTranslation: number[] = [-3.0, -6.0];
          expect(getTranslation(matrix)).toEqual(expectedTranslation);
      });
  });
});
