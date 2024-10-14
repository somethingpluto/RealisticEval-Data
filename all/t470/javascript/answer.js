const math = require('mathjs');

function applyShearX(matrix, shearFactor) {
    /**
     * Applies a shear transformation to a 2D matrix along the x-axis.
     *
     * @param {Array<Array<number>>} matrix - A 2D array representing the original matrix.
     * @param {number} shearFactor - The factor by which the matrix is sheared along the x-axis.
     * @returns {Array<Array<number>>} The sheared matrix.
     */

    let shearMatrix = math.matrix([
        [1, shearFactor],
        [0, 1]
    ]);

    return math.multiply(shearMatrix, matrix);
}