function eulerToRotationMatrix(roll, pitch, yaw) {
    /**
     * Convert Euler angles (roll, pitch, yaw) to a rotation matrix.
     *
     * @param {number} roll - Rotation around the x-axis in degrees.
     * @param {number} pitch - Rotation around the y-axis in degrees.
     * @param {number} yaw - Rotation around the z-axis in degrees.
     *
     * @returns {Array<Array<number>>} A 3x3 rotation matrix.
     */

    // Convert degrees to radians
    const radRoll = (roll * Math.PI) / 180;
    const radPitch = (pitch * Math.PI) / 180;
    const radYaw = (yaw * Math.PI) / 180;

    // Rotation matrix around x-axis (roll)
    const Rx = [
        [1, 0, 0],
        [0, Math.cos(radRoll), -Math.sin(radRoll)],
        [0, Math.sin(radRoll), Math.cos(radRoll)]
    ];

    // Rotation matrix around y-axis (pitch)
    const Ry = [
        [Math.cos(radPitch), 0, Math.sin(radPitch)],
        [0, 1, 0],
        [-Math.sin(radPitch), 0, Math.cos(radPitch)]
    ];

    // Rotation matrix around z-axis (yaw)
    const Rz = [
        [Math.cos(radYaw), -Math.sin(radYaw), 0],
        [Math.sin(radYaw), Math.cos(radYaw), 0],
        [0, 0, 1]
    ];

    // Combined rotation matrix, R = Rz * Ry * Rx
    const R = multiplyMatrices(Rz, multiplyMatrices(Ry, Rx));

    return R;
}

// Helper function to multiply two matrices
function multiplyMatrices(a, b) {
    const result = [];
    for (let i = 0; i < a.length; i++) {
        result[i] = [];
        for (let j = 0; j < b[0].length; j++) {
            let sum = 0;
            for (let k = 0; k < b.length; k++) {
                sum += a[i][k] * b[k][j];
            }
            result[i][j] = sum;
        }
    }
    return result;
}