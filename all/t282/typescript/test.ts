describe('flattenArray', () => {
  it('should flatten a two-dimensional array', () => {
    const input: any[][] = [[1, 2], [3, 4]];
    const expectedOutput: number[] = [1, 2, 3, 4];
    expect(flattenArray(input)).toEqual(expectedOutput);
  });

  it('should flatten a three-dimensional array', () => {
    const input: any[][][] = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]];
    const expectedOutput: number[] = [1, 2, 3, 4, 5, 6, 7, 8];
    expect(flattenArray(input)).toEqual(expectedOutput);
  });

  it('should handle an empty array', () => {
    const input: any[][] = [];
    const expectedOutput: number[] = [];
    expect(flattenArray(input)).toEqual(expectedOutput);
  });

  it('should handle an array with mixed types', () => {
    const input: any[][] = [[1, 'a'], ['b', 2]];
    const expectedOutput: any[] = [1, 'a', 'b', 2];
    expect(flattenArray(input)).toEqual(expectedOutput);
  });
});