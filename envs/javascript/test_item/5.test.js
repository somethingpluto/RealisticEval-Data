/**
 * Implements matrix multiplication.
 * 
 * @param {Array<Array<number>>} matrixA - Matrix A
 * @param {Array<Array<number>>} matrixB - Matrix B
 * @returns {Array<Array<number>>} The result of multiplying matrixA by matrixB
 */
function matrixMultiply(matrixA, matrixB) {
    const rowsA = matrixA.length;
    const colsA = matrixA[0].length;
    const rowsB = matrixB.length;
    const colsB = matrixB[0].length;

    if (colsA !== rowsB) {
        throw new Error("Matrix dimensions do not match for multiplication.");
    }

    const result = new Array(rowsA).fill(0).map(() => new Array(colsB).fill(0));

    for (let i = 0; i < rowsA; i++) {
        for (let j = 0; j < colsB; j++) {
            for (let k = 0; k < colsA; k++) {
                result[i][j] += matrixA[i][k] * matrixB[k][j];
            }
        }
    }

    return result;
}
describe('TestMatrixMultiplication', () => {
    it('should correctly multiply standard matrices', () => {
        const mat1 = [[1, 2], [3, 4]];
        const mat2 = [[5, 6], [7, 8]];
        const expected = [[19, 22], [43, 50]];
        expect(matrixMultiply(mat1, mat2)).toEqual(expected);
    });

    it('multiplying by the identity matrix should yield the answer matrix', () => {
        const mat1 = [[1, 0], [0, 1]];
        const mat2 = [[5, 6], [7, 8]];
        const expected = [[5, 6], [7, 8]];
        expect(matrixMultiply(mat1, mat2)).toEqual(expected);
    });

    it('multiplying by the zero matrix should yield a zero matrix', () => {
        const mat1 = [[0, 0], [0, 0]];
        const mat2 = [[5, 6], [7, 8]];
        const expected = [[0, 0], [0, 0]];
        expect(matrixMultiply(mat1, mat2)).toEqual(expected);
    });

    it('the multiplication of two square matrices should yield the correct product', () => {
        const mat1 = [[1, 2], [3, 4]];
        const mat2 = [[5, 6], [7, 8]];
        const expected = [[19, 22], [43, 50]];
        expect(matrixMultiply(mat1, mat2)).toEqual(expected);
    });

    it('multiplying by the larger identity matrix should yield the answer matrix', () => {
        const mat1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]];
        const mat2 = [[5, 6, 7], [8, 9, 10], [11, 12, 13]];
        const expected = [[5, 6, 7], [8, 9, 10], [11, 12, 13]];
        expect(matrixMultiply(mat1, mat2)).toEqual(expected);
    });
});
