function getScale(matrix: number[][]): [number, number] {
    /**
     * Given a 3x3 affine transformation matrix, return the corresponding scaling factors
     * along the x and y axes.
     *
     * @param matrix - A 3x3 affine transformation matrix.
     * @returns A tuple containing the scale factors (scaleX, scaleY).
     */

    if (matrix.length !== 3 || matrix.some(row => row.length !== 3)) {
        throw new Error("Input must be a 3x3 matrix");
    }

    const scaleX = Math.sqrt(matrix[0][0] ** 2 + matrix[1][0] ** 2);
    const scaleY = Math.sqrt(matrix[0][1] ** 2 + matrix[1][1] ** 2);

    return [scaleX, scaleY];
}
