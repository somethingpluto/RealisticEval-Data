describe('TestLengthOfLIS', () => {
  it('should return 0 for an empty list', () => {
      expect(lengthOfLIS([])).toBe(0);
  });

  it('should return 1 for a list containing only one element', () => {
      expect(lengthOfLIS([7])).toBe(1);
  });

  it('should return 5 for a strictly increasing sequence', () => {
      expect(lengthOfLIS([1, 2, 3, 4, 5])).toBe(5);
  });

  it('should return 1 for a strictly decreasing sequence', () => {
      expect(lengthOfLIS([5, 4, 3, 2, 1])).toBe(1);
  });

  it('should return 4 for a complex sequence with mix of increasing and decreasing elements', () => {
      expect(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])).toBe(4);
  });

  it('should return 1 for a list with all elements being equal', () => {
      expect(lengthOfLIS([2, 2, 2, 2])).toBe(1);
  });

  it('should return 4 for a mix of negative and positive numbers', () => {
      expect(lengthOfLIS([-1, -2, -3, 0, 1, 2])).toBe(4);
  });
});