import * as math from 'mathjs';

function getRotation(matrix: number[][]): number {
  if (matrix.length !== 2 || matrix[0].length !== 3 || matrix[1].length !== 3) {
    throw new Error('Matrix must be a 2x3 affine transformation matrix.');
  }

  const cosTheta = matrix[0][0];
  const sinTheta = matrix[0][1];

  // Calculate the angle using the arctangent function
  // and handle the case where the angle is 180 degrees
  const theta = math.atan2(sinTheta, cosTheta);

  return theta;
}
import * as math from 'mathjs';

describe('TestGetRotationFunction', () => {
    it('test_rotation_0_degrees', () => {
        const matrix = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ];
        const expectedRotation = 0.0;
        expect(getRotation(matrix)).toBeCloseTo(expectedRotation, 6);
    });

    it('test_rotation_90_degrees', () => {
        const matrix = [
            [0, -1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ];
        const expectedRotation = math.PI / 2; // 90 degrees in radians
        expect(getRotation(matrix)).toBeCloseTo(expectedRotation, 6);
    });

    it('test_rotation_180_degrees', () => {
        const matrix = [
            [-1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ];
        const expectedRotation = math.PI; // 180 degrees in radians
        expect(getRotation(matrix)).toBeCloseTo(expectedRotation, 6);
    });

    it('test_rotation_negative_90_degrees', () => {
        const matrix = [
            [0, 1, 0],
            [-1, 0, 0],
            [0, 0, 1]
        ];
        const expectedRotation = -math.PI / 2; // -90 degrees in radians
        expect(getRotation(matrix)).toBeCloseTo(expectedRotation, 6);
    });
});
