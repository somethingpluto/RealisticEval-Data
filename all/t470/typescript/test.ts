import { describe, it, expect } from '@jest/globals';
import { applyShearX } from './path-to-your-function'; // Adjust the path accordingly

describe('applyShearX', () => {
  it('should apply shear transformation along the x-axis correctly', () => {
    const matrix = [
      [1, 0],
      [0, 1]
    ];
    const shearFactor = 0.5;
    const expectedMatrix = [
      [1 + 0.5 * 0, 0.5],
      [0, 1]
    ];

    const result = applyShearX(matrix, shearFactor);

    expect(result).toEqual(expectedMatrix);
  });

  it('should handle different input sizes correctly', () => {
    const matrix = [
      [1, 2, 3],
      [4, 5, 6]
    ];
    const shearFactor = -0.25;
    const expectedMatrix = [
      [1 - 0.25 * 2, 2 - 0.25 * 3, 3],
      [4 - 0.25 * 2, 5 - 0.25 * 3, 6]
    ];

    const result = applyShearX(matrix, shearFactor);

    expect(result).toEqual(expectedMatrix);
  });
});
