function parseMarkdownTable(mdTable: string): Array<[string, ...string[]]> {
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