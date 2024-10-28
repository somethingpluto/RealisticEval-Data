const math = require('mathjs');

describe('TestGetScaleFunction', () => {
    it('test for the identity matrix (no scaling)', () => {
        const matrix = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ];
        const expectedScale = [1.0, 1.0];
        expect(getScale(matrix)).toEqual(expectedScale);
    });

    it('test for a scaling matrix (2x in x and 3x in y)', () => {
        const matrix = [
            [2, 0, 0],
            [0, 3, 0],
            [0, 0, 1]
        ];
        const expectedScale = [2.0, 3.0];
        expect(getScale(matrix)).toEqual(expectedScale);
    });

    it('test case with uniform scaling', () => {
        const matrix = [
            [2, 0, 0],
            [0, 2, 0],
            [0, 0, 1]
        ];
        const expectedScale = [2.0, 2.0];
        expect(getScale(matrix)).toEqual(expectedScale);
    });

    it('test case with non-uniform scaling', () => {
        const matrix = [
            [3, 0, 0],
            [0, 5, 0],
            [0, 0, 1]
        ];
        const expectedScale = [3.0, 5.0];
        expect(getScale(matrix)).toEqual(expectedScale);
    });

    it('test case with reflection matrix', () => {
        const matrix = [
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ];
        const expectedScale = [1.0, 1.0];
        expect(getScale(matrix)).toEqual(expectedScale);
    });
});