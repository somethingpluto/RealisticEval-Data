function matrixVectorMultiplication(matrix: number[][], vector: number[]): number[] {
    /**
     * Multiplies a given matrix by a vector using a nested loop approach.
     *
     * Parameters:
     * matrix (number[][]): A 2D array (matrix) of shape (m, n) where m is the number of rows
                             and n is the number of columns.
     * vector (number[]): A 1D array (vector) of shape (n,) that represents a vector
                         compatible for multiplication with the given matrix.
     *
     * Returns:
     * number[]: A 1D array (resulting vector) of shape (m,) representing the product of
                 the matrix and the vector.
     */

    // Check if the number of columns in the matrix matches the length of the vector
    if (matrix[0].length !== vector.length) {
        throw new Error("The number of columns in the matrix must match the length of the vector.");
    }

    const m = matrix.length;
    const n = vector.length;

    // Initialize the resulting vector with zeros
    const result: number[] = new Array(m).fill(0);

    // Perform matrix-vector multiplication using nested loops
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            result[i] += matrix[i][j] * vector[j];
        }
    }

    // Return the resulting vector from the multiplication
    return result;
}

import * as math from 'mathjs';

describe('TestMatrixVectorMultiplication', () => {
  it('test_case_1', () => {
    // Test with a simple 2x2 matrix and a 2-element vector
    const matrix: number[][] = [[1, 2], [3, 4]];
    const vector: number[] = [5, 6];
    const expectedResult: number[] = [17, 39];  // [1*5 + 2*6, 3*5 + 4*6]
    expect(matrixVectorMultiplication(matrix, vector)).toEqual(expectedResult);
  });

  it('test_case_2', () => {
    // Test with a 3x3 matrix and a 3-element vector
    const matrix: number[][] = [[1, 0, 2], [0, 1, 2], [1, 1, 0]];
    const vector: number[] = [3, 4, 5];
    const expectedResult: number[] = [13, 14, 7];  // [1*3 + 0*4 + 2*5, 0*3 + 1*4 + 2*5, 1*3 + 1*4 + 0*5]
    expect(matrixVectorMultiplication(matrix, vector)).toEqual(expectedResult);
  });

  it('test_case_3', () => {
    // Test with a zero matrix and a vector
    const matrix: number[][] = [[0, 0], [0, 0]];
    const vector: number[] = [1, 1];
    const expectedResult: number[] = [0, 0];  // Zero matrix multiplied by any vector yields zero
    expect(matrixVectorMultiplication(matrix, vector)).toEqual(expectedResult);
  });

  it('test_case_4', () => {
    // Test with a matrix having negative values
    const matrix: number[][] = [[-1, -2], [-3, -4]];
    const vector: number[] = [1, 1];
    const expectedResult: number[] = [-3, -7];  // [-1*1 + -2*1, -3*1 + -4*1]
    expect(matrixVectorMultiplication(matrix, vector)).toEqual(expectedResult);
  });

  it('test_case_5', () => {
    // Test with non-square matrix (2x3) and a compatible vector (3-element)
    const matrix: number[][] = [[1, 2, 3], [4, 5, 6]];
    const vector: number[] = [1, 0, 1];
    const expectedResult: number[] = [4, 10];  // [1*1 + 2*0 + 3*1, 4*1 + 5*0 + 6*1]
    expect(matrixVectorMultiplication(matrix, vector)).toEqual(expectedResult);
  });
});
