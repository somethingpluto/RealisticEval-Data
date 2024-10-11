describe('power function', () => {
    it('should compute the n-th power of a matrix using the fast exponentiation method', () => {
      const matrix = [
        [1, 2],
        [3, 4]
      ];
      const n = 2;
      const expected = [
        [7, 10],
        [15, 22]
      ];
  
      expect(power(matrix, n)).toEqual(expected);
    });
  
    it('should throw an error if n is negative', () => {
      const matrix = [
        [1, 2],
        [3, 4]
      ];
      const n = -1;
  
      expect(() => power(matrix, n)).toThrow('n must be a non-negative integer');
    });
  
    it('should throw an error if matrix is not a list of lists', () => {
      const matrix = 'not a matrix';
      const n = 2;
  
      expect(() => power(matrix, n)).toThrow('matrix must be a list of lists');
    });
  
    it('should throw an error if n is not an integer', () => {
      const matrix = [
        [1, 2],
        [3, 4]
      ];
      const n = 'not an integer';
  
      expect(() => power(matrix, n)).toThrow('n must be a non-negative integer');
    });
  });