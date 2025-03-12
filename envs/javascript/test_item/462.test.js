/**
 * Given a 2D matrix, return all elements of the matrix in spiral order.
 * 
 * @param {number[][]} matrix - A 2D array of integers.
 * @returns {number[]} - An array of integers representing the matrix elements in spiral order.
 */
function spiralOrder(matrix) {
    if (matrix.length === 0) return [];

    let result = [];
    let top = 0, bottom = matrix.length - 1;
    let left = 0, right = matrix[0].length - 1;

    while (top <= bottom && left <= right) {
        // Traverse from left to right along the top row
        for (let i = left; i <= right; i++) {
            result.push(matrix[top][i]);
        }
        top++;

        // Traverse from top to bottom along the right column
        for (let i = top; i <= bottom; i++) {
            result.push(matrix[i][right]);
        }
        right--;

        if (top <= bottom) {
            // Traverse from right to left along the bottom row
            for (let i = right; i >= left; i--) {
                result.push(matrix[bottom][i]);
            }
            bottom--;
        }

        if (left <= right) {
            // Traverse from bottom to top along the left column
            for (let i = bottom; i >= top; i--) {
                result.push(matrix[i][left]);
            }
            left++;
        }
    }

    return result;
}
describe('Test Spiral Order', () => {
  it('should handle an empty matrix', () => {
      expect(spiralOrder([])).toEqual([]);
  });

  it('should handle a single row matrix', () => {
      expect(spiralOrder([[1, 2, 3]])).toEqual([1, 2, 3]);
  });

  it('should handle a single column matrix', () => {
      expect(spiralOrder([[1], [2], [3]])).toEqual([1, 2, 3]);
  });

  it('should handle a square matrix', () => {
      expect(spiralOrder([
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
      ])).toEqual([1, 2, 3, 6, 9, 8, 7, 4, 5]);
  });

  it('should handle a rectangle matrix', () => {
      expect(spiralOrder([
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]
      ])).toEqual([1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]);
  });
});
