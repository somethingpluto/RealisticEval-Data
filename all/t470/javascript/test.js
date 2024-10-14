const applyShearX = require('./path/to/your/applyShearX'); // Adjust the path accordingly

describe('applyShearX', () => {
    it('should apply a shear transformation to a 2D matrix along the x-axis', () => {
        const matrix = [
            [1, 2],
            [3, 4]
        ];
        const shearFactor = 0.5;
        const expected = [
            [1, 2.5],
            [3, 4.5]
        ];

        expect(applyShearX(matrix, shearFactor)).toEqual(expected);
    });

    it('should handle negative shear factors correctly', () => {
        const matrix = [
            [1, 2],
            [3, 4]
        ];
        const shearFactor = -0.5;
        const expected = [
            [1, 1.5],
            [3, 2.5]
        ];

        expect(applyShearX(matrix, shearFactor)).toEqual(expected);
    });

    it('should handle matrices with different dimensions correctly', () => {
        const matrix = [
            [1, 2, 3],
            [4, 5, 6]
        ];
        const shearFactor = 1.0;
        const expected = [
            [1, 3, 5],
            [4, 7, 10]
        ];

        expect(applyShearX(matrix, shearFactor)).toEqual(expected);
    });
});
