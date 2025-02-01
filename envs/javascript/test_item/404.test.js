/**
 * Computes the n-th power of a matrix using the fast exponentiation method.
 * 
 * @param {Array<Array<number>>} matrix - A square matrix to be exponentiated.
 * @param {number} n - The exponent to raise the matrix to. Must be a non-negative integer.
 * 
 * @returns {Array<Array<number>>} The matrix raised to the power of n.
 * 
 * @throws {Error} If n is negative.
 * @throws {TypeError} If matrix is not a list of lists or n is not an integer.
 */
function power(matrix, n) {
    if (!Array.isArray(matrix) || matrix.some(row => !Array.isArray(row) || row.some(cell => typeof cell !== 'number'))) {
        throw new TypeError('Matrix must be a list of lists of numbers.');
    }
    if (!Number.isInteger(n) || n < 0) {
        throw new Error('Exponent must be a non-negative integer.');
    }
    if (n === 0) {
        return matrix.map(row => row.map(() => 1));
    }
    if (n === 1) {
        return matrix;
    }
    if (n % 2 === 0) {
        const halfPower = power(matrix, n / 2);
        return multiply(halfPower, halfPower);
    } else {
        const halfPower = power(matrix, Math.floor(n / 2));
        return multiply(multiply(halfPower, halfPower), matrix);
    }
}

function multiply(a, b) {
    const result = [];
    for (let i = 0; i < a.length; i++) {
        result[i] = [];
        for (let j = 0; j < b[0].length; j++) {
            let sum = 0;
            for (let k = 0; k < a[0].length; k++) {
                sum += a[i][k] * b[k][j];
            }
            result[i][j] = sum;
        }
    }
    return result;
}
describe('TestMatrixPower', () => {
  describe('test_identity_matrix', () => {
      it('should return the identity matrix when raised to the power of 1', () => {
          const matrix = [[1, 0], [0, 1]];
          const expected = [[1, 0], [0, 1]];
          const result = power(matrix, 1);
          expect(result).toEqual(expected);
      });
  });

  describe('test_zero_power', () => {
      it('should return the identity matrix when raised to the power of 0', () => {
          const matrix = [[2, 3], [1, 4]];
          const expected = [[1, 0], [0, 1]];
          const result = power(matrix, 0);
          expect(result).toEqual(expected);
      });
  });

  describe('test_positive_power', () => {
      it('should correctly compute the power of a matrix', () => {
          const matrix = [[2, 1], [1, 3]];
          const expected = [[5, 5], [5, 10]]; // This is the result of matrix^2
          const result = power(matrix, 2);
          expect(result).toEqual(expected);
      });
  });

  describe('test_negative_power', () => {
      it('should throw an error when raised to a negative power', () => {
          const matrix = [[2, 1], [1, 3]];
          expect(() => power(matrix, -1)).toThrow('The exponent n must be a non-negative integer.');
      });
  });
});
