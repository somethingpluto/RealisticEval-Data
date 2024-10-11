class MatrixTraversal {
    constructor() {}

    spiralTraversal(matrix) {
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
         * in the order they were traversed.
         */

        if (!matrix || matrix.length === 0 || matrix[0].length === 0) {
            return [];
        }

        let result = [];
        let top = 0;
        let bottom = matrix.length - 1;
        let left = 0;
        let right = matrix[0].length - 1;

        while (top <= bottom && left <= right) {
            // Traverse from left to right along the top row
            for (let i = left; i <= right; i++) {
                result.push(matrix[top][i]);
            }
            top++;

            // Traverse downwards along the right column
            for (let i = top; i <= bottom; i++) {
                result.push(matrix[i][right]);
            }
            right--;

            // Traverse from right to left along the bottom row, if still within bounds
            if (top <= bottom) {
                for (let i = right; i >= left; i--) {
                    result.push(matrix[bottom][i]);
                }
                bottom--;
            }

            // Traverse upwards along the left column, if still within bounds
            if (left <= right) {
                for (let i = bottom; i >= top; i--) {
                    result.push(matrix[i][left]);
                }
                left++;
            }
        }

        return result;
    }
}