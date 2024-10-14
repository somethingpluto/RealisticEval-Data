function applyShearX(matrix: number[][], shearFactor: number): number[][] {
    /**
     * Applies a shear transformation to a 2D matrix along the x-axis.
     *
     * @param matrix - A 2D array representing the original matrix.
     * @param shearFactor - The factor by which the matrix is sheared along the x-axis.
     *
     * @returns The sheared matrix.
     */

    // Create an empty 2D array with the same dimensions as the input matrix
    let resultMatrix: number[][] = new Array(matrix.length).fill(0).map(() => new Array(matrix[0].length).fill(0));

    for(let i=0; i<matrix.length; i++) {
        for(let j=0; j<matrix[i].length; j++) {
            // Apply the shear transformation formula
            resultMatrix[i][j] = matrix[i][j] + shearFactor * matrix[i][j-1];
        }
    }

    return resultMatrix;
}