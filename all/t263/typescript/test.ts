describe('MatrixTraversal', () => {

  it('should return an empty list for an empty matrix', () => {
    // 异常值测试：空矩阵
    expect(spiralTraversal([])).toEqual([]);
  });

  it('should return the single element in the matrix', () => {
    // 基本逻辑功能测试：单元素矩阵
    const matrix = [[42]];
    expect(spiralTraversal(matrix)).toEqual([42]);
  });

  it('should return all elements in a single row', () => {
    // 边界值测试：单行矩阵
    const matrix = [[1, 2, 3, 4, 5]];
    expect(spiralTraversal(matrix)).toEqual([1, 2, 3, 4, 5]);
  });

  it('should return all elements in a single column', () => {
    // 边界值测试：单列矩阵
    const matrix = [[1], [2], [3], [4], [5]];
    expect(spiralTraversal(matrix)).toEqual([1, 2, 3, 4, 5]);
  });

  it('should return elements in spiral order for a general case matrix', () => {
    // 基本逻辑功能测试：多行多列矩阵
    const matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
    expect(spiralTraversal(matrix)).toEqual([1, 2, 3, 6, 9, 8, 7, 4, 5]);
  });
});