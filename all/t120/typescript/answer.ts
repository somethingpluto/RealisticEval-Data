function extractCSVDataFromHTML(document: Document): string[][] {
    const table = document.querySelector<HTMLTableElement>("table.waffle");
    const result: string[][] = [];

    if (!table) {
        console.error("CSV table not found.");
        return result;
    }

    const rows = table.querySelectorAll<HTMLTableRowElement>("tbody tr");

    rows.forEach(row => {
        const rowData = Array.from(row.querySelectorAll<HTMLTableCellElement>("td"))
                             .map(td => td.textContent?.trim() || '');
        result.push(rowData);
    });

    return result;
}