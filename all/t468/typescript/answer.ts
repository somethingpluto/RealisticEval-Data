function getTranslation(matrix: number[][]): number[] {
    if (matrix.length !== 3 || !matrix.every(row => row.length === 3)) {
        throw new Error('Input must be a 3x3 matrix');
    }
    return [matrix[0][2], matrix[1][2]];
}
