import { Matrix } from './Matrix';

/**
 * Implements matrix multiplication.
 * 
 * @param matrixA - The first matrix.
 * @param matrixB - The second matrix.
 * @returns The result of multiplying matrixA by matrixB.
 */
function matrixMultiply(matrixA: number[][], matrixB: number[][]): number[][] {
  if (matrixA[0].length !== matrixB.length) {
    throw new Error('Incompatible matrix dimensions for multiplication.');
  }

  const result: number[][] = new Array(matrixA.length).fill(0).map(() => new Array(matrixB[0].length).fill(0));

  for (let i = 0; i < matrixA.length; i++) {
    for (let j = 0; j < matrixB[0].length; j++) {
      for (let k = 0; k < matrixA[0].length; k++) {
        result[i][j] += matrixA[i][k] * matrixB[k][j];
      }
    }
  }

  return result;
}
describe('TestMatrixMultiplication', () => {
    test('should correctly multiply standard matrices', () => {
        const mat1 = [[1, 2], [3, 4]];
        const mat2 = [[5, 6], [7, 8]];
        const expected = [[19, 22], [43, 50]];
        expect(matrixMultiply(mat1, mat2)).toEqual(expected);
    });

    test('should yield the answer matrix when multiplying by the identity matrix', () => {
        const mat1 = [[1, 0], [0, 1]];
        const mat2 = [[5, 6], [7, 8]];
        const expected = [[5, 6], [7, 8]];
        expect(matrixMultiply(mat1, mat2)).toEqual(expected);
    });

    test('should yield a zero matrix when multiplying by the zero matrix', () => {
        const mat1 = [[0, 0], [0, 0]];
        const mat2 = [[5, 6], [7, 8]];
        const expected = [[0, 0], [0, 0]];
        expect(matrixMultiply(mat1, mat2)).toEqual(expected);
    });

    test('should yield the correct product when multiplying two square matrices', () => {
        const mat1 = [[1, 2], [3, 4]];
        const mat2 = [[5, 6], [7, 8]];
        const expected = [[19, 22], [43, 50]];
        expect(matrixMultiply(mat1, mat2)).toEqual(expected);
    });

    test('should yield the answer matrix when multiplying by a larger identity matrix', () => {
        const mat1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]];
        const mat2 = [[5, 6, 7], [8, 9, 10], [11, 12, 13]];
        const expected = [[5, 6, 7], [8, 9, 10], [11, 12, 13]];
        expect(matrixMultiply(mat1, mat2)).toEqual(expected);
    });
});
