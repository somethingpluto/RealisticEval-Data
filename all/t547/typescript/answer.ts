function calculateColumnWidths(data: string[][]): number[] {
    // Initialize a list to hold the maximum widths for each column.
    // This assumes that all rows in data have the same number of columns.
    const widths: number[] = new Array(data[0].length).fill(0);

    // Iterate over each row in the data.
    for (const row of data) {
        // Iterate over each column in the row.
        for (let idx = 0; idx < row.length; idx++) {
            // Update the width at index `idx` with the maximum of the current width
            // and the length of the string in the current column.
            widths[idx] = Math.max(widths[idx], row[idx].length);
        }
    }

    // Return the list of maximum widths for each column.
    return widths;
}