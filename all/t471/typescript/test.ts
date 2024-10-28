import * as math from 'mathjs';

describe('TestGetRotationFunction', () => {
    it('test_rotation_0_degrees', () => {
        const matrix = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ];
        const expectedRotation = 0.0;
        expect(getRotation(matrix)).toBeCloseTo(expectedRotation, 6);
    });

    it('test_rotation_90_degrees', () => {
        const matrix = [
            [0, -1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ];
        const expectedRotation = math.PI / 2; // 90 degrees in radians
        expect(getRotation(matrix)).toBeCloseTo(expectedRotation, 6);
    });

    it('test_rotation_180_degrees', () => {
        const matrix = [
            [-1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ];
        const expectedRotation = math.PI; // 180 degrees in radians
        expect(getRotation(matrix)).toBeCloseTo(expectedRotation, 6);
    });

    it('test_rotation_negative_90_degrees', () => {
        const matrix = [
            [0, 1, 0],
            [-1, 0, 0],
            [0, 0, 1]
        ];
        const expectedRotation = -math.PI / 2; // -90 degrees in radians
        expect(getRotation(matrix)).toBeCloseTo(expectedRotation, 6);
    });
});