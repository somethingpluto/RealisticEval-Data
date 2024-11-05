function spiral_traversal(matrix) {
    /**
     * Traverse a given m x n matrix in a spiral order and return all elements as an array.
     *
     * The function starts at the top-left corner of the matrix and traverses it in a
     * clockwise spiral order, moving right across the top row, down the right column,
     * left across the bottom row, and up the left column, repeating this process
     * until all elements are traversed.
     *
     * @param {number[][]} matrix - A 2D array representing the matrix with m rows and n columns.
     * @returns {number[]} An array of numbers representing the elements of the matrix
     *                      in the order they were traversed.
     */
    if (!matrix.length) {
        return [];
    }

    const m = matrix.length;
    const n = matrix[0].length;
    let rowStart = 0, rowEnd = m - 1;
    let colStart = 0, colEnd = n - 1;
    let result = [];

    while (rowStart <= rowEnd && colStart <= colEnd) {
        // Traverse Right along the top row
        for (let j = colStart; j <= colEnd; j++) {
            result.push(matrix[rowStart][j]);
        }
        rowStart++;

        // Traverse Down along the right column
        for (let i = rowStart; i <= rowEnd; i++) {
            result.push(matrix[i][colEnd]);
        }
        colEnd--;

        // Traverse Left along the bottom row, if still within bounds
        if (rowStart <= rowEnd) {
            for (let j = colEnd; j >= colStart; j--) {
                result.push(matrix[rowEnd][j]);
            }
            rowEnd--;
        }

        // Traverse Up along the left column, if still within bounds
        if (colStart <= colEnd) {
            for (let i = rowEnd; i >= rowStart; i--) {
                result.push(matrix[i][colStart]);
            }
            colStart++;
        }
    }

    return result;
}