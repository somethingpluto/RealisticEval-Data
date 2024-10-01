function createMatrix(rows, columns, initialValue) {
    // Initialize the matrix as an empty array
    const matrix = [];

    // Loop through each row
    for (let i = 0; i < rows; i++) {
        // Create a new row array
        const row = [];

        // Loop through each column and fill the row with the initial value
        for (let j = 0; j < columns; j++) {
            row.push(initialValue);
        }

        // Add the filled row to the matrix
        matrix.push(row);
    }

    return matrix;
}