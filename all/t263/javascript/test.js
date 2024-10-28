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