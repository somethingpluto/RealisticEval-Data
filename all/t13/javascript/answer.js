function parseMarkdownTable(mdTable) {
    /**
     * Parses a Markdown formatted table into an array of tuples, each tuple representing a row.
     *
     * @param {string} mdTable - A string representing a Markdown table.
     * @returns {Array<Array<string>>} An array where each sub-array represents a row in the table.
     */
    
    // Split the input string into lines and trim whitespace
    const lines = mdTable.trim().split('\n');

    // Filter out the separator line for the header (which usually contains "---")
    const filteredLines = lines.filter(line => !line.trim().includes('---'));

    // Initialize the array to store each row as a tuple (sub-array)
    const tableData = [];

    // Process each line
    for (const line of filteredLines) {
        // Trim leading and trailing spaces and pipes, then split by "|"
        const row = line.trim().replace(/^\|+|\|+$/g, '').split('|');
        
        // Process each cell, trim spaces, handle empty cells, and create a tuple (sub-array)
        const tupleRow = row.map(cell => cell.trim() || '');
        
        // Add the tuple (sub-array) to the array
        tableData.push(tupleRow);
    }

    return tableData;
}