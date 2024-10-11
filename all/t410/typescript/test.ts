describe('check_xor_sum', () => {
    it('should return true for valid combinations', () => {
      const combination = np.array([
        [1, 0, 1],
        [0, 1, 0],
        [1, 1, 1]
      ]);
  
      const result = check_xor_sum(combination);
      expect(result).toBe(true);
    });
  
    it('should return false for invalid combinations', () => {
      const combination = np.array([
        [1, 0, 1],
        [0, 1, 0],
        [0, 0, 0]
      ]);
  
      const result = check_xor_sum(combination);
      expect(result).toBe(false);
    });
  });
  