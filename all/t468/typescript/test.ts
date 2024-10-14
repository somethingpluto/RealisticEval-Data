import { expect } from '@jest/globals';
import * as np from 'numpy'; // Assuming you have a way to import numpy or mock it

// Mock the numpy module if needed
const mockNumpy = {
  ndarray: jest.fn(),
  zeros: jest.fn().mockReturnValue(np.ndarray([0, 0])),
};

jest.mock('numpy', () => mockNumpy);

describe('get_translation function', () => {
  it('should extract translation vector from a 3x3 affine transformation matrix', () => {
    // Arrange
    const matrix = np.ndarray([
      [1, 0, 5],
      [0, 1, 3],
      [0, 0, 1],
    ]);

    // Act
    const result = get_translation(matrix);

    // Assert
    expect(result).toEqual(np.ndarray([5, 3]));
  });

  it('should handle identity matrix correctly', () => {
    // Arrange
    const matrix = np.ndarray([
      [1, 0, 0],
      [0, 1, 0],
      [0, 0, 1],
    ]);

    // Act
    const result = get_translation(matrix);

    // Assert
    expect(result).toEqual(np.ndarray([0, 0]));
  });
});

function get_translation(matrix: np.ndarray): np.ndarray {
  /**
   * Given a 3x3 matrix, return the corresponding translation vector.
   *
   * Args:
   *     matrix (np.ndarray): A 3x3 affine transformation matrix.
   *
   * Returns:
   *     np.ndarray: A 2-element array containing the translation components (translation_x, translation_y).
   */
  return np.ndarray([matrix[2][0], matrix[2][1]]);
}