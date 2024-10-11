describe('calculateTotalSeconds', () => {
  it('should return the total number of seconds for [1, 2, 3, 4]', () => {
    const result = calculateTotalSeconds([1, 2, 3, 4]);
    expect(result).toBe(93784);
  });

  it('should return the total number of seconds for [0, 2, 3]', () => {
    const result = calculateTotalSeconds([0, 2, 3]);
    expect(result).toBe(7380);
  });
});