describe('TestLengthOfLIS', () => {
    it('should handle an empty list', () => {
      expect(lengthOfLIS([])).toBe(0);
    });
  
    it('should handle a list with a single element', () => {
      expect(lengthOfLIS([7])).toBe(1);
    });
  
    it('should handle a strictly increasing sequence', () => {
      expect(lengthOfLIS([1, 2, 3, 4, 5])).toBe(5);
    });
  
    it('should handle a strictly decreasing sequence', () => {
      expect(lengthOfLIS([5, 4, 3, 2, 1])).toBe(1);
    });
  
    it('should handle a complex sequence with a mix of increasing and decreasing elements', () => {
      expect(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])).toBe(4);
    });
  
    it('should handle a list with all elements being equal', () => {
      expect(lengthOfLIS([2, 2, 2, 2])).toBe(1);
    });
  
    it('should handle a mix of negative and positive numbers', () => {
      expect(lengthOfLIS([-1, -2, -3, 0, 1, 2])).toBe(4);
    });
  });