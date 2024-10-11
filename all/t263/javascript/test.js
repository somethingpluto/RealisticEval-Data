describe('Matrix Traversal', () => {
  it('should traverse a 3x3 matrix in spiral order', () => {
    const matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ];
    expect(spiralTraversal(matrix)).toEqual([1, 2, 3, 6, 9, 8, 7, 4, 5]);
  });

  it('should handle a 2x2 matrix', () => {
    const matrix = [
      [1, 2],
      [3, 4]
    ];
    expect(spiralTraversal(matrix)).toEqual([1, 2, 4, 3]);
  });

  it('should handle a 1x1 matrix', () => {
    const matrix = [[1]];
    expect(spiralTraversal(matrix)).toEqual([1]);
  });

  it('should handle an empty matrix', () => {
    const matrix = [];
    expect(spiralTraversal(matrix)).toEqual([]);
  });
});