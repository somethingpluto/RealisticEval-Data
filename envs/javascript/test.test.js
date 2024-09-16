/**
 * Extract table question from a document object containing HTML tables and return the question organized as a two-dimensional array.
 * @param {document} document
 */
function extractCSVDataFromHTML(document) {
  const tables = document.querySelectorAll('table');
  const data = [];
  
  for (let i = 0; i < tables.length; i++) {
    const table = tables[i];
    const rows = table.querySelectorAll('tr');
    
    for (let j = 0; j < rows.length; j++) {
      const row = rows[j];
      const cells = row.querySelectorAll('td');
      
      for (let k = 0; k < cells.length; k++) {
        const cell = cells[k];
        const value = cell.textContent.trim();
        
        if (value.length > 0) {
          data.push([value]);
        }
      }
    }
  }
  
  return data;
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
