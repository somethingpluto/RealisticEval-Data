function spiralTraversal(matrix: number[][]): number[] {
  const result: number[] = [];
  let top = 0, bottom = matrix.length - 1;
  let left = 0, right = matrix[0].length - 1;

  while (top <= bottom && left <= right) {
    for (let i = left; i <= right; i++) {
      result.push(matrix[top][i]);
    }
    top++;

    for (let i = top; i <= bottom; i++) {
      result.push(matrix[i][right]);
    }
    right--;

    if (top <= bottom) {
      for (let i = right; i >= left; i--) {
        result.push(matrix[bottom][i]);
      }
      bottom--;
    }

    if (left <= right) {
      for (let i = bottom; i >= top; i--) {
        result.push(matrix[i][left]);
      }
      left++;
    }
  }

  return result;
}
describe('MatrixTraversal', () => {
  
  
    it('should return an empty list for an empty matrix', () => {
      // 异常值测试：空矩阵
      expect(spiralTraversal([])).toEqual([], 'Should return an empty list for an empty matrix');
    });
  
    it('should return the single element in the matrix', () => {
      // 基本逻辑功能测试：单元素矩阵
      const matrix = [[42]];
      expect(spiralTraversal(matrix)).toEqual([42], 'Should return the single element in the matrix');
    });
  
    it('should return all elements in a single row', () => {
      // 边界值测试：单行矩阵
      const matrix = [[1, 2, 3, 4, 5]];
      expect(spiralTraversal(matrix)).toEqual([1, 2, 3, 4, 5], 'Should return all elements in a single row');
    });
  
    it('should return all elements in a single column', () => {
      // 边界值测试：单列矩阵
      const matrix = [[1], [2], [3], [4], [5]];
      expect(spiralTraversal(matrix)).toEqual([1, 2, 3, 4, 5], 'Should return all elements in a single column');
    });
  
    it('should return elements in spiral order for a general case matrix', () => {
      // 基本逻辑功能测试：多行多列矩阵
      const matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
      expect(spiralTraversal(matrix)).toEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], 'Should return elements in spiral order for a general case matrix');
    });
  });
