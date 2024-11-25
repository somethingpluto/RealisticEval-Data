function applyShearX(matrix, shearFactor) {
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