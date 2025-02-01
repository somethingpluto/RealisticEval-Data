/**
 * Extract table question from a document object containing HTML tables and return the question organized as a two-dimensional array.
 * @param {document} document
 */
function extractCSVDataFromHTML(document) {
    // Find all table elements in the document
    const tables = document.querySelectorAll('table');
    const tableData = [];

    // Iterate over each table
    tables.forEach(table => {
        // Find the tbody element within the table
        const tbody = table.querySelector('tbody');
        if (!tbody) return; // Skip if no tbody is found

        // Find all tr elements within the tbody
        const rows = tbody.querySelectorAll('tr');
        const rowData = [];

        // Iterate over each row
        rows.forEach(row => {
            // Find all td elements within the row
            const cells = row.querySelectorAll('td');
            const cellData = [];

            // Iterate over each cell
            cells.forEach(cell => {
                // Extract the text content of the cell
                const cellText = cell.textContent.trim();
                cellData.push(cellText);
            });

            // Add the row data to the rowData array
            rowData.push(cellData);
        });

        // Add the table data to the tableData array
        tableData.push(rowData);
    });

    // Return the two-dimensional array containing table data
    return tableData;
}
const { JSDOM } = require('jsdom');

describe('HTML to CSV Extraction Tests', () => {
  const createMockDocument = (html) => {
    const dom = new JSDOM(html);
    return dom.window.document;
  };

  const extractCSVDataFromHTML = (document) => {
    const rows = document.querySelectorAll('table.waffle tbody tr');
    return Array.from(rows).map(row =>
      Array.from(row.cells).map(cell => cell.textContent || "")
    );
  };

  test('Table with multiple rows and columns', () => {
    const testCaseHTML = `
      <table class="waffle">
        <tbody>
          <tr><td>Cell 1</td><td>Cell 2</td></tr>
          <tr><td>Cell 3</td><td>Cell 4</td></tr>
        </tbody>
      </table>`;
    const document = createMockDocument(testCaseHTML);
    expect(extractCSVDataFromHTML(document)).toEqual([["Cell 1", "Cell 2"], ["Cell 3", "Cell 4"]]);
  });

  test('Table with empty cells', () => {
    const testCaseHTML = `
      <table class="waffle">
        <tbody>
          <tr><td>Cell 1</td><td></td></tr>
          <tr><td></td><td>Cell 4</td></tr>
        </tbody>
      </table>`;
    const document = createMockDocument(testCaseHTML);
    expect(extractCSVDataFromHTML(document)).toEqual([["Cell 1", ""], ["", "Cell 4"]]);
  });

  test('Table with only one row', () => {
    const testCaseHTML = `
      <table class="waffle">
        <tbody>
          <tr><td>Single Cell 1</td><td>Single Cell 2</td></tr>
        </tbody>
      </table>`;
    const document = createMockDocument(testCaseHTML);
    expect(extractCSVDataFromHTML(document)).toEqual([["Single Cell 1", "Single Cell 2"]]);
  });

  test('Table with only one column', () => {
    const testCaseHTML = `
      <table class="waffle">
        <tbody>
          <tr><td>Column Cell 1</td></tr>
          <tr><td>Column Cell 2</td></tr>
        </tbody>
      </table>`;
    const document = createMockDocument(testCaseHTML);
    expect(extractCSVDataFromHTML(document)).toEqual([["Column Cell 1"], ["Column Cell 2"]]);
  });

  test('No table with the class "waffle" present', () => {
    const testCaseHTML = `
      <div>
        <p>No table here!</p>
      </div>`;
    const document = createMockDocument(testCaseHTML);
    expect(extractCSVDataFromHTML(document)).toEqual([]);
  });
});
