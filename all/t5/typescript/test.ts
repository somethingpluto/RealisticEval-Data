import { matrixMultiply } from './yourModule'; // Make sure to adjust the import based on your setup

describe('Matrix Multiplication', () => {
    it('should correctly multiply standard matrices', () => {
        const mat1 = [[1, 2], [3, 4]];
        const mat2 = [[5, 6], [7, 8]];
        const expected = [[19, 22], [43, 50]];
        expect(matrixMultiply(mat1, mat2)).toEqual(expected);
    });

    it('should handle empty matrices without error', () => {
        const mat1: number[][] = [];
        const mat2: number[][] = [];
        const expected: number[][] = [];
        expect(matrixMultiply(mat1, mat2)).toEqual(expected);
    });

    it('should yield the original matrix when multiplying by the identity matrix', () => {
        const mat1 = [[1, 0], [0, 1]];
        const mat2 = [[5, 6], [7, 8]];
        const expected = [[5, 6], [7, 8]];
        expect(matrixMultiply(mat1, mat2)).toEqual(expected);
    });
});