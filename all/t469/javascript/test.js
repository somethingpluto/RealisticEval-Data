// Import necessary packages
const { describe, it, expect } = require('@jest/globals');

// Mock NumPy library if needed
// For simplicity, let's assume we're not using any external libraries here

function getScale(matrix) {
    // Implement the logic similar to the Python function
    // This is just a placeholder implementation
    const scaleX = Math.sqrt(matrix[0][0] ** 2 + matrix[0][1] ** 2);
    const scaleY = Math.sqrt(matrix[1][0] ** 2 + matrix[1][1] ** 2);
    return [scaleX, scaleY];
}

describe('getScale', () => {
    it('should return correct scale factors for a valid 3x3 matrix', () => {
        const matrix = [
            [2, 0, 0],
            [0, 3, 0],
            [0, 0, 1]
        ];
        const expected = [2, 3];
        const result = getScale(matrix);
        expect(result).toEqual(expected);
    });

    it('should handle zero scaling correctly', () => {
        const matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ];
        const expected = [0, 0];
        const result = getScale(matrix);
        expect(result).toEqual(expected);
    });

    it('should throw error for non-3x3 matrix', () => {
        const matrix = [
            [2, 0],
            [0, 3]
        ];
        expect(() => getScale(matrix)).toThrow('Matrix must be 3x3');
    });
});