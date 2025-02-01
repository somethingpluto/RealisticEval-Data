/**
 * Given an affine transformation matrix, return the corresponding rotation angle in radians.
 *
 * @param {Array<Array<number>>} matrix - A 2D affine transformation matrix.
 * @returns {number} The rotation angle in radians, extracted from the affine matrix.
 */
function getRotation(matrix) {
  // Extract the relevant components of the affine matrix
  const a = matrix[0][0];
  const b = matrix[0][1];
  const c = matrix[1][0];
  const d = matrix[1][1];

  // Calculate the rotation angle using the arctangent function
  const angle = Math.atan2(b, a);

  // Return the rotation angle in radians
  return angle;
}
const assert = require('assert');

describe('TestGetRotationFunction', () => {
    it('test_rotation_0_degrees', () => {
        // Test for a rotation of 0 degrees (identity matrix)
        const matrix = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ];
        const expectedRotation = 0.0;
        expect(getRotation(matrix)).toBeCloseTo(expectedRotation, 6);
    });

    it('test_rotation_90_degrees', () => {
        // Test for a rotation of 90 degrees
        const matrix = [
            [0, -1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ];
        const expectedRotation = Math.PI / 2;  // 90 degrees in radians
        expect(getRotation(matrix)).toBeCloseTo(expectedRotation, 6);
    });

    it('test_rotation_180_degrees', () => {
        // Test for a rotation of 180 degrees
        const matrix = [
            [-1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ];
        const expectedRotation = Math.PI;  // 180 degrees in radians
        expect(getRotation(matrix)).toBeCloseTo(expectedRotation, 6);
    });

    it('test_rotation_negative_90_degrees', () => {
        // Test for a rotation of -90 degrees
        const matrix = [
            [0, 1, 0],
            [-1, 0, 0],
            [0, 0, 1]
        ];
        const expectedRotation = -Math.PI / 2;  // -90 degrees in radians
        expect(getRotation(matrix)).toBeCloseTo(expectedRotation, 6);
    });
});
