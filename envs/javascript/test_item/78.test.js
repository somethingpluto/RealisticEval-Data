/**
 * Convert Euler angles (roll, pitch, yaw) to a rotation matrix.
 *
 * @param {number} roll - Rotation around the x-axis in degrees.
 * @param {number} pitch - Rotation around the y-axis in degrees.
 * @param {number} yaw - Rotation around the z-axis in degrees.
 *
 * @returns {Array<Array<number>>} A 3x3 rotation matrix.
 */
function eulerToRotationMatrix(roll, pitch, yaw) {
    // Convert degrees to radians
    const toRadians = (angle) => angle * (Math.PI / 180);

    // Convert Euler angles to radians
    const rollRad = toRadians(roll);
    const pitchRad = toRadians(pitch);
    const yawRad = toRadians(yaw);

    // Calculate the rotation matrix components
    const cosRoll = Math.cos(rollRad);
    const sinRoll = Math.sin(rollRad);
    const cosPitch = Math.cos(pitchRad);
    const sinPitch = Math.sin(pitchRad);
    const cosYaw = Math.cos(yawRad);
    const sinYaw = Math.sin(yawRad);

    // Construct the rotation matrix
    const rotationMatrix = [
        [
            cosYaw * cosPitch,
            cosYaw * sinPitch * sinRoll - sinYaw * cosRoll,
            cosYaw * sinPitch * cosRoll + sinYaw * sinRoll,
        ],
        [
            sinYaw * cosPitch,
            sinYaw * sinPitch * sinRoll + cosYaw * cosRoll,
            sinYaw * sinPitch * cosRoll - cosYaw * sinRoll,
        ],
        [
            -sinPitch,
            cosPitch * sinRoll,
            cosPitch * cosRoll,
        ],
    ];

    return rotationMatrix;
}
describe('TestEulerToRotationMatrix', () => {
    it('test_zero_rotation', () => {
        // Test with zero rotation for all axes
        const R = eulerToRotationMatrix(0, 0, 0);
        expect(R).toEqual([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]);
    });

    it('test_rotation_about_x', () => {
        // Test rotation about the x-axis
        const R = eulerToRotationMatrix(90, 0, 0);
        const expected = [
            [1, 0, 0],
            [0, 0, -1],
            [0, 1, 0]
        ];
        expect(R).toEqual(expected);
    });

    it('test_rotation_about_y', () => {
        // Test rotation about the y-axis
        const R = eulerToRotationMatrix(0, 90, 0);
        const expected = [
            [0, 0, 1],
            [0, 1, 0],
            [-1, 0, 0]
        ];
        expect(R).toEqual(expected);
    });

    it('test_rotation_about_z', () => {
        // Test rotation about the z-axis
        const R = eulerToRotationMatrix(0, 0, 90);
        const expected = [
            [0, -1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ];
        expect(R).toEqual(expected);
    });

    it('test_combined_rotation', () => {
        // Test combined rotation
        const R = eulerToRotationMatrix(30, 45, 60);
        const expected = [
            [0.35355339, -0.5732233, 0.73919892],
            [0.61237244, 0.73919892, 0.28033009],
            [-0.70710678, 0.35355339, 0.61237244]
        ];
        expect(R).toEqual(expected);
    });
});
