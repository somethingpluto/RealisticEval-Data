import { expect } from '@jest/globals';
import { matrixVectorMultiplication } from './path-to-your-matrix-vector-multiplication-file'; // Adjust the path accordingly

describe('Matrix-Vector Multiplication', () => {
    it('should correctly multiply a matrix by a vector', () => {
        const matrix = [
            [1, 2, 3],
            [4, 5, 6]
        ];
        const vector = [7, 8, 9];
        const expected = [50, 122];

        const result = matrixVectorMultiplication(matrix, vector);

        expect(result).toEqual(expected);
    });

    it('should handle empty vectors and matrices', () => {
        const matrix = [];
        const vector = [];
        const expected = [];

        const result = matrixVectorMultiplication(matrix, vector);

        expect(result).toEqual(expected);
    });

    it('should throw an error if the dimensions do not match', () => {
        const matrix = [
            [1, 2, 3],
            [4, 5, 6]
        ];
        const vector = [7, 8]; // Incorrect dimension
        const expectedError = 'Dimension mismatch';

        expect(() => matrixVectorMultiplication(matrix, vector)).toThrow(expectedError);
    });
});
