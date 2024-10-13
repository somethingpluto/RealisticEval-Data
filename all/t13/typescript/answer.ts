function parseMarkdownTable(mdTable: string): Array<[string]> {
    /**
     * Parses a Markdown formatted table into an array of tuples, each tuple representing a row.
     *
     * @param mdTable - A string representing a Markdown table.
     * @returns An array where each tuple represents a row in the table.
     */
    // Split the input string into lines and strip whitespace
    const lines = mdTable.trim().split('\n');

    // Filter out the separator line for the header (which usually contains "---")
    const filteredLines = lines.filter(line => !line.trim().includes('---'));

    // Initialize the array to store each row as a tuple
    const tableData: Array<[string]> = [];

    // Process each line
    for (const line of filteredLines) {
        // Strip leading and trailing spaces and pipes, then split by "|"
        const row = line.trim().replace(/^\|+|\|+$/g, '').split('|');
        // Process each cell, strip spaces, handle empty cells, and create a tuple
        const tupleRow: [string] = row.map(cell => cell.trim() || '').filter(cell => cell !== '') as [string];
        // Add the tuple to the array
        tableData.push(tupleRow);
    }

    return tableData;
}