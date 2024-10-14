function calculateColumnWidths(data) {
    // Initialize an array to hold the maximum widths for each column.
    // This assumes that all rows in data have the same number of columns.
    let widths = new Array(data[0].length).fill(0);

    // Iterate over each row in the data.
    for (let row of data) {
        // Iterate over each column in the row.
        for (let idx = 0; idx < row.length; idx++) {
            // Update the width at index `idx` with the maximum of the current width
            // and the length of the string in the current column.
            widths[idx] = Math.max(widths[idx], row[idx].toString().length);
        }
    }

    // Return the array of maximum widths for each column.
    return widths;
}