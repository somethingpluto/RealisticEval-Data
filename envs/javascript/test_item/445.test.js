/**
 * Create a pose matrix representing a rotation about a given axis.
 *
 * @param {number} angleDeg - Rotation angle in degrees.
 * @param {string} axis - Axis to rotate about, must be one of 'X', 'Y', or 'Z'.
 * @returns {Array<Array<number>>} - 4x4 pose matrix representing the rotation.
 */
function createRotMatrix(angleDeg, axis) {
    // Convert angle from degrees to radians
    const angleRad = angleDeg * (Math.PI / 180);

    // Initialize the 4x4 identity matrix
    const matrix = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ];

    // Calculate the sine and cosine of the angle
    const cos = Math.cos(angleRad);
    const sin = Math.sin(angleRad);

    // Modify the matrix based on the axis of rotation
    switch (axis) {
        case 'X':
            matrix[1][1] = cos;
            matrix[1][2] = -sin;
            matrix[2][1] = sin;
            matrix[2][2] = cos;
            break;
        case 'Y':
            matrix[0][0] = cos;
            matrix[0][2] = sin;
            matrix[2][0] = -sin;
            matrix[2][2] = cos;
            break;
        case 'Z':
            matrix[0][0] = cos;
            matrix[0][1] = -sin;
            matrix[1][0] = sin;
            matrix[1][1] = cos;
            break;
        default:
            throw new Error("Invalid axis. Must be one of 'X', 'Y', or 'Z'.");
    }

    return matrix;
}
describe('TestCreateRotMatrix', () => {
    it('test_rotation_x_90_degrees', () => {
        /** Test rotation around X-axis for 90 degrees */
        const expectedMatrix = [
            [1, 0, 0, 0],
            [0, 0, -1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
        ];
        const resultMatrix = createRotMatrix(90, 'x');
        expect(resultMatrix).toEqual(expectedMatrix);
    });

    it('test_rotation_y_180_degrees', () => {
        /** Test rotation around Y-axis for 180 degrees */
        const expectedMatrix = [
            [-1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, -1, 0],
            [0, 0, 0, 1]
        ];
        const resultMatrix = createRotMatrix(180, 'y');
        expect(resultMatrix).toEqual(expectedMatrix);
    });

    it('test_rotation_z_270_degrees', () => {
        /** Test rotation around Z-axis for 270 degrees (or -90 degrees) */
        const expectedMatrix = [
            [0, 1, 0, 0],
            [-1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ];
        const resultMatrix = createRotMatrix(270, 'z');
        expect(resultMatrix).toEqual(expectedMatrix);
    });

    it('test_invalid_axis', () => {
        /** Test behavior with invalid axis input */
        expect(() => createRotMatrix(90, 'a')).toThrow('Invalid axis. Must be one of \'X\', \'Y\', or \'Z\'.');
    });

    it('test_zero_rotation', () => {
        /** Test zero degree rotation which should lead to identity matrix */
        const expectedMatrix = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ];
        const resultMatrix = createRotMatrix(0, 'x');
        expect(resultMatrix).toEqual(expectedMatrix);
    });
});
