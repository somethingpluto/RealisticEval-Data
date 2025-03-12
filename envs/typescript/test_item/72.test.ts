// ... (previous code for context)
export function get3DCoordinates(K: number[][], d: number, x: number, y: number): [number, number, number] {
    if (!isValidCameraMatrix(K)) {
        throw new Error('Invalid camera matrix');
    }
    // ... (rest of the function)
}

function isValidCameraMatrix(K: number[][]): boolean {
    if (K.length !== 3 || K[0].length !== 3 || K[1].length !== 3 || K[2].length !== 3) {
        return false;
    }
    return true;
}
// ... (rest of the code)
describe('TestGet3DCoordinates', () => {
    let K: number[][];

    beforeEach(() => {
        // Define a common intrinsic matrix for testing
        K = [
            [1000, 0, 320],
            [0, 1000, 240],
            [0, 0, 1]
        ];
    });

    it('test_center_coordinates', () => {
        // Test with center pixel coordinates where x and y should map to zero in NDC.
        const result = get3DCoordinates(K, 100, 320, 240);
        expect(result).toEqual([0.0, 0.0, 100]);
    });

    it('test_boundary_coordinates', () => {
        // Test with boundary values in the image frame.
        const result = get3DCoordinates(K, 50, 640, 480);
        const expected_x = (640 - 320) / 1000 * 50;
        const expected_y = (480 - 240) / 1000 * 50;
        expect(result).toEqual([expected_x, expected_y, 50]);
    });

    it('test_negative_depth', () => {
        // Test with a negative depth to see if it handles incorrect input properly.
        const result = get3DCoordinates(K, -100, 320, 240);
        expect(result).toEqual([0.0, 0.0, -100]);
    });

    it('test_zero_depth', () => {
        // Test with zero depth which should lead to a zero-length vector.
        const result = get3DCoordinates(K, 0, 320, 240);
        expect(result).toEqual([0.0, 0.0, 0.0]);
    });

    it('test_non_integer_values', () => {
        // Test with non-integer pixel coordinates.
        const result = get3DCoordinates(K, 100, 320.5, 240.5);
        const expected_x = (320.5 - 320) / 1000 * 100;
        const expected_y = (240.5 - 240) / 1000 * 100;
        expect(result).toEqual([expected_x, expected_y, 100]);
    });
});
