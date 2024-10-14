import { describe, it, expect } from '@jest/globals';
import { getRotation } from './path-to-your-function'; // Adjust the path accordingly
import * as np from 'numpy'; // Assuming you have a compatible npm package for numpy

describe('getRotation', () => {
  it('should correctly extract the rotation angle from a 2D affine transformation matrix', () => {
    const matrix = np.array([
      [1, 0, 0],
      [0, 1, 0],
      [0, 0, 1]
    ]);

    const result = getRotation(matrix);
    expect(result).toBeCloseTo(0); // Assuming the rotation should be 0 radians for the given identity matrix
  });

  it('should handle other matrices with known rotation angles', () => {
    const matrix = np.array([
      [Math.cos(Math.PI / 4), -Math.sin(Math.PI / 4), 0],
      [Math.sin(Math.PI / 4), Math.cos(Math.PI / 4), 0],
      [0, 0, 1]
    ]);

    const result = getRotation(matrix);
    expect(result).toBeCloseTo(Math.PI / 4); // Assuming the rotation should be π/4 radians for the given matrix
  });
})