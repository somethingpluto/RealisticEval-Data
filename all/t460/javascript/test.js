const matrixVectorMultiplication = require('./matrixVectorMultiplication'); // replace with actual path

describe('Matrix Vector Multiplication', () => {
    it('should multiply a matrix by a vector', () => {
        const matrix = [[1, 2], [3, 4]];
        const vector = [5, 6];
        const expected = [17, 39];

        expect(matrixVectorMultiplication(matrix, vector)).toEqual(expected);
    });

    it('should throw an error if dimensions are incompatible', () => {
        const matrix = [[1, 2], [3, 4]];
        const vector = [5];

        expect(() => matrixVectorMultiplication(matrix, vector)).toThrowError();
    });
});
