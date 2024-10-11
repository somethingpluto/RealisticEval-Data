describe('power', () => {
    it('should return the correct result for positive exponents', () => {
      const matrix = [
        [1, 2],
        [3, 4]
      ];
      const n = 2;
      const expected = [
        [7, 10],
        [15, 22]
      ];
  
      // Assuming you have implemented the 'power' function in TypeScript
      const result = power(matrix, n);
  
      expect(result).toEqual(expected);
    });
  
    it('should throw error for negative exponents', () => {
      const matrix = [
        [1, 2],
        [3, 4]
      ];
      const n = -1;
  
      // Assuming you have implemented the 'power' function in TypeScript
      expect(() => power(matrix, n)).toThrowError('n must be a non-negative integer');
    });
  });