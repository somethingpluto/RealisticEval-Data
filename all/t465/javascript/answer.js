function matrixVectorMultiplication(matrix, vector) {
    /*
    Multiplies a given matrix by a vector.

    Parameters:
    matrix (Array<Array<number>>): A 2D array (matrix) of shape (m, n) where m is the number of rows
                                    and n is the number of columns.
    vector (Array<number>): A 1D array (vector) of length n that represents a vector
                            compatible for multiplication with the given matrix.

    Returns:
    Array<number>: A 1D array (resulting vector) of length m representing the product of
                   the matrix and the vector.
    */

    // Initialize an empty array for the result vector.
    let result = [];

    // Iterate over each row in the matrix.
    for(let i=0; i<matrix.length; i++) {
        // Initialize sum for current row.
        let sum = 0;

        // Multiply elements of current row with corresponding elements of vector.
        for(let j=0; j<matrix[i].length; j++) {
            sum += matrix[i][j] * vector[j];
        }

        // Push sum to result vector.
        result.push(sum);
    }

    // Return the resulting vector.
    return result;
}