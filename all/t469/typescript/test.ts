import { get_scale } from './getScale';

describe('get_scale', () => {
    it('should correctly calculate scale factors for a given 3x3 affine transformation matrix', () => {
        const matrix: number[][] = [
            [2, 0, 0],
            [0, 3, 0],
            [0, 0, 1]
        ];

        const expected: [number, number] = [2, 3];

        const result = get_scale(matrix);

        expect(result).toEqual(expected);
    });

    it('should handle matrices with non-zero translation components', () => {
        const matrix: number[][] = [
            [2, 0, 5],
            [0, 3, 7],
            [0, 0, 1]
        ];

        const expected: [number, number] = [2, 3];

        const result = get_scale(matrix);

        expect(result).toEqual(expected);
    });

    it('should handle singular matrices (zero scaling)', () => {
        const matrix: number[][] = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ];

        const expected: [number, number] = [0, 0];

        const result = get_scale(matrix);

        expect(result).toEqual(expected);
    });
});
