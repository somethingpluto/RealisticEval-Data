import assert from 'assert';
describe('TestGet3DCoordinates', () => {
    let K;

    beforeEach(() => {
        // Define a common intrinsic matrix for testing
        K = [
            [1000, 0, 320],
            [0, 1000, 240],
            [0, 0, 1]
        ];
    });

    it('test center coordinates', () => {
        // Test with center pixel coordinates where x and y should map to zero in NDC.
        const result = get3DCoordinates(K, 100, 320, 240);
        assert.deepStrictEqual(result, [0.0, 0.0, 100]);
    });

    it('test boundary coordinates', () => {
        // Test with boundary values in the image frame.
        const result = get3DCoordinates(K, 50, 640, 480);
        const expected_x = (640 - 320) / 1000 * 50;
        const expected_y = (480 - 240) / 1000 * 50;
        assert.deepStrictEqual(result, [expected_x, expected_y, 50]);
    });


    it('test zero depth', () => {
        // Test with zero depth which should lead to a zero-length vector.
        const result = get3DCoordinates(K, 0, 320, 240);
        assert.deepStrictEqual(result, [0.0, 0.0, 0.0]);
    });

    it('test non-integer values', () => {
        // Test with non-integer pixel coordinates.
        const result = get3DCoordinates(K, 100, 320.5, 240.5);
        const expected_x = (320.5 - 320) / 1000 * 100;
        const expected_y = (240.5 - 240) / 1000 * 100;
        assert.deepStrictEqual(result, [expected_x, expected_y, 100]);
    });
});