const { mat4 } = require('gl-matrix');

function getRotation(matrix) {
    /**
     * Given an affine transformation matrix, return the corresponding rotation angle in radians.
     *
     * @param {Array} matrix - A 2D affine transformation matrix.
     * @returns {number} The rotation angle in radians, extracted from the affine matrix.
     */

    // Extract the rotation component from the matrix
    const rotationMatrix = [
        [matrix[0], matrix[1]],
        [matrix[3], matrix[4]]
    ];

    // Calculate the trace of the rotation matrix
    const trace = rotationMatrix[0][0] + rotationMatrix[1][1];

    // Calculate the determinant of the rotation matrix
    const det = rotationMatrix[0][0] * rotationMatrix[1][1] - rotationMatrix[0][1] * rotationMatrix[1][0];

    // Calculate the rotation angle in radians
    let rotationAngle;

    if (det >= 0) {
        rotationAngle = Math.atan2(rotationMatrix[1][0], rotationMatrix[0][0]);
    } else {
        rotationAngle = Math.PI - Math.atan2(-rotationMatrix[1][0], -rotationMatrix[0][0]);
    }

    return rotationAngle;
}

// Example usage:
const matrix = [
    1, 0, 0, 0,
    0, 1, 0, 0,
    0, 0, 1, 0,
    0, 0, 0, 1
];

console.log(getRotation(matrix));
