/**
 * Traverse a given m x n matrix in a spiral order and return all elements as an array.
 *
 * The function starts at the top-left corner of the matrix and traverses it in a
 * clockwise spiral order, moving right across the top row, down the right column,
 * left across the bottom row, and up the left column, repeating this process
 * until all elements are traversed.
 *
 * @param {number[][]} matrix - A 2D array representing the matrix with m rows and n columns.
 * @returns {number[]} An array of numbers representing the elements of the matrix
 *                     in the order they were traversed.
 */
function spiral_traversal(matrix) {
    if (matrix.length === 0) return [];

    let result = [];
    let top = 0, bottom = matrix.length - 1, left = 0, right = matrix[0].length - 1;

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

        // Make sure we are still within the bounds of the matrix
        if (top <= bottom) {
            // Traverse from right to left along the bottom row
            for (let i = right; i >= left; i--) {
                result.push(matrix[bottom][i]);
            }
            bottom--;
        }

        // Make sure we are still within the bounds of the matrix
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
describe('MatrixTraversal', () => {

  it('should handle an empty matrix', () => {
      // 异常值测试：空矩阵
      expect(spiral_traversal([])).toEqual([], 'Should return an empty list for an empty matrix');
  });

  it('should handle a single element matrix', () => {
      // 基本逻辑功能测试：单元素矩阵
      const matrix = [[42]];
      expect(spiral_traversal(matrix)).toEqual([42], 'Should return the single element in the matrix');
  });

  it('should handle a single row matrix', () => {
      // 边界值测试：单行矩阵
      const matrix = [[1, 2, 3, 4, 5]];
      expect(spiral_traversal(matrix)).toEqual([1, 2, 3, 4, 5], 'Should return all elements in a single row');
  });

  it('should handle a single column matrix', () => {
      // 边界值测试：单列矩阵
      const matrix = [[1], [2], [3], [4], [5]];
      expect(spiral_traversal(matrix)).toEqual([1, 2, 3, 4, 5], 'Should return all elements in a single column');
  });

  it('should handle a general case matrix', () => {
      // 基本逻辑功能测试：多行多列矩阵
      const matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
      expect(spiral_traversal(matrix)).toEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], 'Should return elements in spiral order for a general case matrix');
  });
});
