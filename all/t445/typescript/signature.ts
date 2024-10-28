import * as math from 'mathjs';

/**
 * Create a pose matrix representing a rotation about a given axis.
 *
 * @param angleDeg - Rotation angle in degrees.
 * @param axis - Axis to rotate about, must be one of 'X', 'Y', or 'Z'.
 * @returns A 4x4 pose matrix representing the rotation.
 */
function createRotMatrix(angleDeg: number, axis: 'X' | 'Y' | 'Z'): number[][] {}