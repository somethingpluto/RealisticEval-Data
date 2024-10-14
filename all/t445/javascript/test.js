const { createRotMatrix } = require('./path-to-your-module'); // Replace with the actual path to your module

describe('createRotMatrix function', () => {
    it('should return a 4x4 rotation matrix for a given angle and axis', () => {
        const angleDeg = 90;
        const axis = 'X';

        const result = createRotMatrix(angleDeg, axis);

        expect(result).toEqual([
            [1, 0, 0, 0],
            [0, 0, -1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
        ]);
    });
});