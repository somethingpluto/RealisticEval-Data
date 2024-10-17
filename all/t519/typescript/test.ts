describe('TestTransposeMatrix', () => {
  it('should transpose a square matrix', () => {
    const matrix = [[1, 2], [3, 4]];
    const expected = [[1, 3], [2, 4]];
    const result = transposeMatrix(matrix);
    expect(result).toEqual(expected);
  });

  it('should transpose a rectangular matrix', () => {
    const matrix = [[1, 2, 3], [4, 5, 6]];
    const expected = [[1, 4], [2, 5], [3, 6]];
    const result = transposeMatrix(matrix);
    expect(result).toEqual(expected);
  });

  it('should handle a matrix with empty rows', () => {
    const matrix = [[], []];
    const expected = [];
    const result = transposeMatrix(matrix);
    expect(result).toEqual(expected);
  });

  it('should transpose a matrix with a single element', () => {
    const matrix = [[5]];
    const expected = [[5]];
    const result = transposeMatrix(matrix);
    expect(result).toEqual(expected);
  });
});