// matrixVectorMultiplication.test.js

const matrixVectorMultiplication = require('./matrixVectorMultiplication');

describe('Matrix-Vector Multiplication', () => {
    test('should multiply a 2x2 matrix by a 2-element vector correctly', () => {
        const matrix = [
            [1, 2],
            [3, 4]
        ];
        const vector = [5, 6];
        const expected = [17, 39];

        expect(matrixVectorMultiplication(matrix, vector)).toEqual(expected);
    });

    test('should handle zero vectors correctly', () => {
        const matrix = [
            [0, 0],
            [0, 0]
        ];
        const vector = [1, 2];
        const expected = [0, 0];

        expect(matrixVectorMultiplication(matrix, vector)).toEqual(expected);
    });

    test('should handle empty vectors correctly', () => {
        const matrix = [];
        const vector = [];
        const expected = [];

        expect(matrixVectorMultiplication(matrix, vector)).toEqual(expected);
    });
});
