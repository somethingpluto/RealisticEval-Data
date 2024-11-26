import * as math from 'mathjs';

/**
 * Given an affine transformation matrix, return the corresponding rotation angle in radians.
 *
 * @param matrix - A 2D affine transformation matrix.
 * @returns The rotation angle in radians, extracted from the affine matrix.
 */
function getRotation(matrix: number[][]): number {
    // Ensure the matrix is a 2D array and has the correct shape
    if (!Array.isArray(matrix) || matrix.length !== 3 || matrix.some(row => row.length !== 3)) {
        throw new Error("Input must be a 3x3 affine transformation matrix.");
    }

    // Calculate the rotation angle using atan2
    const rotationAngle = math.atan2(matrix[1][0], matrix[0][0]);

    return rotationAngle;
}