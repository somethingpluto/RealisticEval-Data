const { describe, it, expect } = require('@jest/globals');
const { getRotation } = require('./path_to_your_module'); // replace with your module path
const np = require('numpy');

describe('getRotation', () => {
    it('should return correct rotation angle for identity matrix', () => {
        const matrix = np.eye(2);
        expect(getRotation(matrix)).toBeCloseTo(0);
    });

    it('should return correct rotation angle for rotation matrix', () => {
        const matrix = np.array([[Math.cos(Math.PI / 4), -Math.sin(Math.PI / 4)], [Math.sin(Math.PI / 4), Math.cos(Math.PI / 4)]]);
        expect(getRotation(matrix)).toBeCloseTo(Math.PI / 4);
    });
});
