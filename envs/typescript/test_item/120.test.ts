import { Document, HTMLTableElement, HTMLTableRowElement, HTMLTableCellElement } from 'dom';

function extractCSVDataFromHTML(document: Document): string[][] {
  const tables: HTMLTableElement[] = Array.from(document.getElementsByTagName('table'));
  const data: string[][] = [];

  tables.forEach(table => {
    const rows: HTMLTableRowElement[] = Array.from(table.getElementsByTagName('tr'));
    rows.forEach(row => {
      const cells: HTMLTableCellElement[] = Array.from(row.getElementsByTagName('td'));
      const rowData: string[] = cells.map(cell => cell.textContent || '').filter(Boolean);
      data.push(rowData);
    });
  });

  return data;
}
import { JSDOM } from 'jsdom';

describe('HTML to CSV Extraction Tests', () => {
  const createMockDocument = (html: string): Document => {
    const dom = new JSDOM(html);
    return dom.window.document;
  };

  const extractCSVDataFromHTML = (document: Document): string[][] => {
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
