import {Matrix} from 'mathjs'
function getTranslation(matrix) {
    if (!(matrix instanceof Matrix)) {
        throw new Error('Input must be a 3x3 matrix');
    }

    const m = matrix.toArray();
    if (m.length !== 9 || m[0].length !== 3) {
        throw new Error('Input must be a 3x3 matrix');
    }

    const translationX = m[2][0];
    const translationY = m[2][1];

    return [translationX, translationY];
}

describe('TestGetTranslationFunction', () => {
    describe('test_identity_matrix', () => {
        it('should return the correct translation for the identity matrix', () => {
            const matrix = [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]
            ];
            const expectedTranslation = [0.0, 0.0];
            expect(getTranslation(matrix)).toEqual(expectedTranslation);
        });
    });

    describe('test_translation_matrix', () => {
        it('should return the correct translation for a translation matrix (5 in x, 10 in y)', () => {
            const matrix = [
                [1, 0, 5],
                [0, 1, 10],
                [0, 0, 1]
            ];
            const expectedTranslation = [5.0, 10.0];
            expect(getTranslation(matrix)).toEqual(expectedTranslation);
        });
    });

    describe('test_negative_translation', () => {
        it('should return the correct translation for a translation matrix with negative values', () => {
            const matrix = [
                [1, 0, -3],
                [0, 1, -6],
                [0, 0, 1]
            ];
            const expectedTranslation = [-3.0, -6.0];
            expect(getTranslation(matrix)).toEqual(expectedTranslation);
        });
    });
});
