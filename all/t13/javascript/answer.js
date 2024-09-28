/**
 * Parses a Markdown formatted table into an array of tuples, each tuple representing a row.
 *
 * @param {string} mdTable - A string representing a Markdown table.
 * @returns {Array} - An array where each tuple (array) represents a row in the table.
 */
function parseMarkdownTable(mdTable) {
    // Split the input string into lines and trim whitespace
    let lines = mdTable.trim().split('\n');

    // Filter out the separator line for the header (which usually contains "---")
    lines = lines.filter(line => !line.trim().includes('---'));

    // Initialize the array to store each row as a tuple (array)
    let tableData = [];

    // Process each line
    for (let line of lines) {
        // Trim leading and trailing spaces and pipes, then split by "|"
        let row = line.trim().replace(/^\|/, '').replace(/\|$/, '').split('|');
        // Process each cell, trim spaces, handle empty cells, and create an array
        let tupleRow = row.map(cell => cell.trim()).map(cell => cell !== '' ? cell : '');
        // Add the tuple to the list
        tableData.push(tupleRow);
    }

    return tableData;
}