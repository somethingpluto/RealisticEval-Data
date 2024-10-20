import { Matrix, math } from 'mathjs';

/**
 * Convert Euler angles (roll, pitch, yaw) to a rotation matrix.
 *
 * @param roll - Rotation around the x-axis in degrees.
 * @param pitch - Rotation around the y-axis in degrees.
 * @param yaw - Rotation around the z-axis in degrees.
 * @returns A 3x3 rotation matrix.
 */
function eulerToRotationMatrix(roll: number, pitch: number, yaw: number): Matrix {
    // Convert degrees to radians
    const rollRad = math.unit(roll, 'deg').toNumber('rad');
    const pitchRad = math.unit(pitch, 'deg').toNumber('rad');
    const yawRad = math.unit(yaw, 'deg').toNumber('rad');

    // Rotation matrix around x-axis (roll)
    const Rx = math.matrix([
        [1, 0, 0],
        [0, math.cos(rollRad), -math.sin(rollRad)],
        [0, math.sin(rollRad), math.cos(rollRad)]
    ]);

    // Rotation matrix around y-axis (pitch)
    const Ry = math.matrix([
        [math.cos(pitchRad), 0, math.sin(pitchRad)],
        [0, 1, 0],
        [-math.sin(pitchRad), 0, math.cos(pitchRad)]
    ]);

    // Rotation matrix around z-axis (yaw)
    const Rz = math.matrix([
        [math.cos(yawRad), -math.sin(yawRad), 0],
        [math.sin(yawRad), math.cos(yawRad), 0],
        [0, 0, 1]
    ]);

    // Combined rotation matrix, R = Rz * Ry * Rx
    const R = math.multiply(Rz, math.multiply(Ry, Rx));

    return R;
}