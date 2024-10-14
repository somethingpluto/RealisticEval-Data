function getTranslation(matrix: number[][]): number[] {
    /**
     * Given a 3x3 matrix, return the corresponding translation vector.
     *
     * @param matrix - A 3x3 affine transformation matrix.
     * @returns A 2-element array containing the translation components (translation_x, translation_y).
     */
    if (matrix.length !== 3 || !matrix.every(row => row.length === 3)) {
        throw new Error('Input must be a 3x3 matrix');
    }
    return [matrix[0][2], matrix[1][2]];
}
