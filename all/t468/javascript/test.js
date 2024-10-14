const { getTranslation } = require('./your-python-module'); // Adjust the path accordingly

describe('getTranslation', () => {
    it('should return the correct translation vector for a given 3x3 matrix', () => {
        const matrix = [
            [1, 0, 5],
            [0, 1, 10],
            [0, 0, 1]
        ];
        const expectedTranslation = [5, 10];
        const result = getTranslation(matrix);
        expect(result).toEqual(expectedTranslation);
    });

    it('should handle matrices with different values', () => {
        const matrix = [
            [2, 0, 7],
            [0, 3, 9],
            [0, 0, 1]
        ];
        const expectedTranslation = [7, 9];
        const result = getTranslation(matrix);
        expect(result).toEqual(expectedTranslation);
    });

    it('should throw an error if the input is not a 3x3 matrix', () => {
        const matrix = [
            [1, 0, 5],
            [0, 1, 10] // Missing third row
        ];

        expect(() => getTranslation(matrix)).toThrowError('Input matrix must be a 3x3 matrix');
    });
});
