describe('TestFindLargestDivisible', () => {
    describe('test_typical_case', () => {
      it('should find the largest divisible number for typical inputs', () => {
        expect(findLargestDivisible(50)).toBe(50);
        expect(findLargestDivisible(47)).toBe(45);
      });
    });
  
    describe('test_no_divisible_found', () => {
      it('should return null when no divisible number is found', () => {
        expect(findLargestDivisible(4)).toBeNull();
      });
    });
  
    describe('test_exact_half_divisible', () => {
      it('should find the largest divisible number when the half of n is exactly divisible by 5', () => {
        expect(findLargestDivisible(10)).toBe(10);
      });
    });
  
    describe('test_large_number', () => {
      it('should find the largest divisible number for large numbers', () => {
        expect(findLargestDivisible(1000)).toBe(1000);
      });
    });
  
    describe('test_lower_bound', () => {
      it('should find the largest divisible number for the lowest bound', () => {
        expect(findLargestDivisible(5)).toBe(5);
      });
    });
  });