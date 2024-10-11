describe('length_of_LIS', () => {
    test('should return 4 for [10, 9, 2, 5, 3, 7, 101, 18]', () => {
      const nums = [10, 9, 2, 5, 3, 7, 101, 18];
      expect(length_of_LIS(nums)).toBe(4);
    });
  
    test('should return 1 for [1]', () => {
      const nums = [1];
      expect(length_of_LIS(nums)).toBe(1);
    });
  
    test('should return 0 for [] (empty array)', () => {
      const nums = [];
      expect(length_of_LIS(nums)).toBe(0);
    });
  
    test('should return 3 for [1, 3, 6, 7] (all elements in increasing order)', () => {
      const nums = [1, 3, 6, 7];
      expect(length_of_LIS(nums)).toBe(4);
    });
  
    test('should return 2 for [10, 22, 9, 33, 21, 50, 41, 60] (mixed order)', () => {
      const nums = [10, 22, 9, 33, 21, 50, 41, 60];
      expect(length_of_LIS(nums)).toBe(5);
    });
  });