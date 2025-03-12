// ... (previous code for context)

function multiplyMatrices(a: number[][], b: number[][]): number[][] {
  if (a[0].length !== b.length) {
    throw new Error('Matrices dimensions do not match for multiplication');
  }

  const result: number[][] = Array.from({ length: a.length }, () => Array(b[0].length).fill(0));

  for (let i = 0; i < a.length; i++) {
    for (let j = 0; j < b[0].length; j++) {
      for (let k = 0; k < a[0].length; k++) {
        result[i][j] += a[i][k] * b[k][j];
      }
    }
  }

  return result;
}

function power(matrix: number[][], n: number): number[][] {
  if (!Number.isInteger(n) || n < 0) {
    throw new Error('Exponent must be a non-negative integer');
  }

  if (n === 0) {
    return identityMatrix(matrix.length);
  }

  let result = identityMatrix(matrix.length);
  let base = matrix;

  while (n > 0) {
    if (n % 2 === 1) {
      result = multiplyMatrices(result, base);
    }
    base = multiplyMatrices(base, base);
    n = Math.floor(n / 2);
  }

  return result;
}

function identityMatrix(size: number): number[][] {
  return Array.from({ length: size }, (_, i) =>
    Array.from({ length: size }, (_, j) => (i === j ? 1 : 0))
  );
}

// ... (rest of the code)
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
