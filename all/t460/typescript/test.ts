import { describe, it, expect } from '@jest/globals';

function matrixVectorMultiplication(matrix: number[][], vector: number[]): number[] {
    // Function implementation here...
}

describe('matrixVectorMultiplication', () => {
    it('should multiply a matrix by a vector correctly', () => {
        const matrix = [[1, 2], [3, 4]];
        const vector = [5, 6];
        const expectedResult = [17, 39];

        const result = matrixVectorMultiplication(matrix, vector);

        expect(result).toEqual(expectedResult);
    });

    it('should throw an error if the dimensions are incompatible', () => {
        const matrix = [[1, 2], [3, 4]];
        const vector = [5]; // Incompatible dimension

        expect(() => matrixVectorMultiplication(matrix, vector)).toThrowError();
    });
});
