/**
 * Multiplies a given matrix by a vector using JavaScript's Array methods.
 *
 * @param {number[][]} matrix - A 2D array (matrix) of shape (m, n) where m is the number of rows
 *                              and n is the number of columns.
 * @param {number[]} vector - A 1D array (vector) of shape (n,) that represents a vector
 *                             compatible for multiplication with the given matrix.
 *
 * @returns {number[]} A 1D array (resulting vector) of shape (m,) representing the product of
 *                    the matrix and the vector.
 */
function matrixVectorMultiplication(matrix, vector) {
    // Check if the dimensions of the matrix and vector allow for multiplication.
    if (matrix[0].length !== vector.length) {
        throw new Error('Matrix and vector dimensions do not match.');
    }

    // Initialize an array to store the result.
    let result = [];

    // Iterate over each row in the matrix.
    for (let i = 0; i < matrix.length; i++) {
        let sum = 0;

        // Iterate over each element in the current row and corresponding element in the vector.
        for (let j = 0; j < matrix[i].length; j++) {
            sum += matrix[i][j] * vector[j];
        }

        // Add the computed value to the result array.
        result.push(sum);
    }

    // Return the resulting vector from the multiplication.
    return result;
}