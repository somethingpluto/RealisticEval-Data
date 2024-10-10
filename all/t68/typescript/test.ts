describe('divideList', () => {
  it('should divide list evenly into n parts', () => {
    const result = divideList([1, 2, 3, 4, 5], 2);
    expect(result).toEqual([[1, 2, 3], [4, 5]]);
  });

  it('should handle list with length not divisible by n', () => {
    const result = divideList([1, 2, 3, 4, 5, 6], 3);
    expect(result).toEqual([[1, 2], [3, 4], [5, 6]]);
  });
});