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
    // Validate input types
    if (!Array.isArray(matrix) || !matrix.every(Array.isArray)) {
        throw new TypeError('Matrix must be a list of lists.');
    }
    if (!Number.isInteger(n)) {
        throw new TypeError('Exponent n must be an integer.');
    }
    if (n < 0) {
        throw new Error('Exponent n must be non-negative.');
    }

    // Helper function to multiply two matrices
    function multiplyMatrices(A, B) {
        const size = A.length;
        const result = Array.from({ length: size }, () => Array(size).fill(0));

        for (let i = 0; i < size; i++) {
            for (let j = 0; j < size; j++) {
                for (let k = 0; k < size; k++) {
                    result[i][j] += A[i][k] * B[k][j];
                }
            }
        }

        return result;
    }

    // Fast exponentiation algorithm
    function fastExponentiation(matrix, n) {
        if (n === 0) {
            // Return the identity matrix of the same size as matrix
            const size = matrix.length;
            return Array.from({ length: size }, (_, i) => 
                Array.from({ length: size }, (_, j) => (i === j ? 1 : 0))
            );
        }

        if (n === 1) {
            return matrix;
        }

        const halfPower = fastExponentiation(matrix, Math.floor(n / 2));
        const result = multiplyMatrices(halfPower, halfPower);

        if (n % 2 === 0) {
            return result;
        } else {
            return multiplyMatrices(result, matrix);
        }
    }

    return fastExponentiation(matrix, n);
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
