describe('TestMatrixPower', () => {
  describe('test_identity_matrix', () => {
      it('should return the identity matrix when the power is 1', () => {
          const matrix: number[][] = [[1, 0], [0, 1]];
          const expected: number[][] = [[1, 0], [0, 1]];
          const result = power(matrix, 1);
          expect(result).toEqual(expected);
      });
  });

  describe('test_zero_power', () => {
      it('should return the identity matrix when the power is 0', () => {
          const matrix: number[][] = [[2, 3], [1, 4]];
          const expected: number[][] = [[1, 0], [0, 1]];
          const result = power(matrix, 0);
          expect(result).toEqual(expected);
      });
  });

  describe('test_positive_power', () => {
      it('should correctly compute the power of a matrix for a positive exponent', () => {
          const matrix: number[][] = [[2, 1], [1, 3]];
          const expected: number[][] = [[5, 5], [5, 10]]; // This is the result of matrix^2
          const result = power(matrix, 2);
          expect(result).toEqual(expected);
      });
  });

  describe('test_negative_power', () => {
      it('should throw an error when the power is negative', () => {
          const matrix: number[][] = [[2, 1], [1, 3]];
          expect(() => power(matrix, -1)).toThrow('The exponent n must be a non-negative integer.');
      });
  });
});