function parseMarkdownTable(mdTable: string): Array<[string, ...string[]]> {
    /**
     * Parses a Markdown formatted table into a list of tuples, each tuple representing a row.
     *
     * Args:
     *     mdTable (string): A string representing a Markdown table.
     *
     * Returns:
     *     Array of tuples: An array where each tuple represents a row in the table.
     */

    // Split the input string into lines and strip whitespace
    const lines = mdTable.trim().split('\n');

    // Filter out the separator line for the header (which usually contains "---")
    const filteredLines = lines.filter(line => !line.trim().includes('---'));

    // Initialize the list to store each row as a tuple
    const tableData: Array<[string, ...string[]]> = [];

    // Process each line
    for (const line of filteredLines) {
        // Strip leading and trailing spaces and pipes, then split by "|"
        const row = line.trim().replace(/^\||\|$/g, '').split('|');
        // Process each cell, strip spaces, handle empty cells, and create a tuple
        const tupleRow = row.map(cell => cell.trim() !== '' ? cell.trim() : '') as [string, ...string[]];
        // Add the tuple to the list
        tableData.push(tupleRow);
    }

    return tableData;
}