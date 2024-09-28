const matrixMultiply = require('./matrixMultiply'); // Adjust the path as needed

describe('Matrix Multiplication', () => {
    test('Standard matrices', () => {
        const mat1 = [[1, 2], [3, 4]];
        const mat2 = [[5, 6], [7, 8]];
        const expected = [[19, 22], [43, 50]];
        expect(matrixMultiply(mat1, mat2)).toEqual(expected);
    });

    test('Empty matrices', () => {
        const mat1 = [];
        const mat2 = [];
        const expected = [];
        expect(matrixMultiply(mat1, mat2)).toEqual(expected);
    });

    test('Identity matrix', () => {
        const mat1 = [[1, 0], [0, 1]];
        const mat2 = [[5, 6], [7, 8]];
        const expected = [[5, 6], [7, 8]];
        expect(matrixMultiply(mat1, mat2)).toEqual(expected);
    });
});