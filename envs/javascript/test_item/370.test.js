/**
 * Decompose a flat index `n` into a multidimensional index based on the given shape.
 *
 * @param {number} n - Flat index (non-negative integer).
 * @param {Array<number>} shape - Array representing the dimensions of the multi-dimensional array.
 * @returns {Array<number>} - Array representing the multidimensional index corresponding to `n`.
 * @throws {Error} - If `n` is out of bounds for the array defined by `shape`.
 */
function decompose(n, shape) {
    // Check if the flat index is out of bounds
    const totalElements = shape.reduce((acc, dim) => acc * dim, 1);
    if (n < 0 || n >= totalElements) {
        throw new Error("Index out of bounds for the given shape.");
    }

    // Initialize the result array
    const result = new Array(shape.length).fill(0);

    // Decompose the flat index into the multidimensional index
    for (let i = shape.length - 1; i >= 0; i--) {
        const dimSize = shape[i];
        result[i] = n % dimSize;
        n = Math.floor(n / dimSize);
    }

    return result;
}
describe('TestDecomposeFunction', () => {
  it('should handle edge case with larger shape', () => {
      expect(decompose(60, [4, 4, 4])).toEqual([3, 3, 0]);
  });

  it('should handle the last valid index', () => {
      expect(decompose(63, [4, 4, 4])).toEqual([3, 3, 3]);
  });

  it('should handle single dimension case', () => {
      expect(decompose(2, [5])).toEqual([2]);
  });

  it('should throw an error for invalid cases', () => {
      // Test case 5: Out of bounds case (negative index)
      expect(() => decompose(-1, [3, 4, 5])).toThrow('Index out of bounds');

      // Test case 6: Out of bounds case (index too large)
      expect(() => decompose(100, [3, 4, 5])).toThrow('Index out of bounds');
  });
});
