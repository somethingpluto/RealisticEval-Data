describe('Flatten Array', () => {
  it('should flatten a two-level nested array', () => {
    const input = [[1, 2], [3, 4]];
    const expectedOutput = [1, 2, 3, 4];
    expect(flattenArray(input)).toEqual(expectedOutput);
  });

  it('should handle an empty array', () => {
    const input = [];
    const expectedOutput = [];
    expect(flattenArray(input)).toEqual(expectedOutput);
  });

  it('should flatten a three-level nested array', () => {
    const input = [[1, 2], [3, [4, 5]]];
    const expectedOutput = [1, 2, 3, 4, 5];
    expect(flattenArray(input)).toEqual(expectedOutput);
  });

  it('should handle an array with non-array elements', () => {
    const input = [1, 'a', [2, null], { key: 'value' }];
    const expectedOutput = [1, 'a', 2, null, { key: 'value' }];
    expect(flattenArray(input)).toEqual(expectedOutput);
  });
});