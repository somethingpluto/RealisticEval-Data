function spiralOrder(matrix: number[][]): number[] {
    /**
     * Given a 2D array, return all elements of the array in spiral order.
     *
     * @param {number[][]} matrix - A 2D array of numbers.
     * @returns {number[]} A list of numbers representing the array elements in spiral order.
     */

    let result: number[] = [];
    while (matrix.length) {
        // Take the first row and remove it from the matrix
        result.push(...matrix.shift());

        // If there's still something left, go right along the last row
        if (matrix.length && matrix[0].length) {
            for (let i = 0; i < matrix.length; i++) {
                result.push(matrix[i].pop());
            }
        }

        // Take the last row and remove it from the matrix
        if (matrix.length) {
            result.push(...matrix.pop().reverse());
        }

        // If there's still something left, go up along the first column
        if (matrix.length && matrix[0].length) {
            for (let i = matrix.length - 1; i >= 0; i--) {
                result.push(matrix[i].shift());
            }
        }
    }
    return result;
}