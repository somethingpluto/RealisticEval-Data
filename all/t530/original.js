// Function to create a matrix where number-of-rows = (end-start) years, number-of-columns = number-of-issues-in-a-year. Created by ChatGPT.
function createMatrix(rows, columns, initialValue) {

    printToConsole("Start: createMatrix()")

    matrix = [];
    for (let i = 0; i < rows; i++) {
        const row = [];
        for (let j = 0; j < columns; j++) {
            row.push(initialValue);
        }
        matrix.push(row);
    }

    printToConsole("End: createMatrix()")
    return matrix;
}