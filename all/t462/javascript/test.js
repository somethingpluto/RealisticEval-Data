const { spiralOrder } = require('./spiralMatrix'); // Assuming your function is in a file named spiralMatrix.js

describe('spiralOrder', () => {
  it('should return the elements of a 2D matrix in spiral order', () => {
    const matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ];
    expect(spiralOrder(matrix)).toEqual([1, 2, 3, 6, 9, 8, 7, 4, 5]);
  });

  it('should handle an empty matrix', () => {
    const matrix = [];
    expect(spiralOrder(matrix)).toEqual([]);
  });

  it('should handle a single row matrix', () => {
    const matrix = [[1, 2, 3]];
    expect(spiralOrder(matrix)).toEqual([1, 2, 3]);
  });

  it('should handle a single column matrix', () => {
    const matrix = [
      [1],
      [2],
      [3]
    ];
    expect(spiralOrder(matrix)).toEqual([1, 2, 3]);
  });
});
