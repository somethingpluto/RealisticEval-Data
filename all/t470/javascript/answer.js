function applyShearX(matrix, shearFactor) {
    /**
     * Applies a shear transformation to a 2D matrix along the x-axis.
     *
     * @param {Array<Array<number>>} matrix - A 2D array representing the original matrix.
     * @param {number} shearFactor - The factor by which the matrix is sheared along the x-axis.
     * @returns {Array<Array<number>>} The sheared matrix.
     */
    
    // Define the shear transformation matrix for shearing along the x-axis
    const shearMatrix = [[1, shearFactor], [0, 1]];

    // Applying the shear transformation
    // For matrix multiplication, we'll implement it manually
    const transformedMatrix = matrix.map(row => {
        return [
            row[0] * shearMatrix[0][0] + row[1] * shearMatrix[1][0],
            row[0] * shearMatrix[0][1] + row[1] * shearMatrix[1][1]
        ];
    });

    return transformedMatrix;
}