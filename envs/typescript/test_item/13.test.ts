// Start of the code context
import { parse } from 'markdown-it';

function parseMarkdownTable(mdTable: string): Array<[string]> {
    const md = new markdownIt();
    const tokens = md.parse(mdTable, {});
    // ... (rest of the original function)

    // New code to handle the additional requirements
    const headers = row.map(token => token.content || '').join('').trim().split('|').map(cell => cell.trim());
    const dataRows = rows.slice(1).map(rowTokens => {
        const cells = rowTokens.map(token => {
            if (token.type === 'text') {
                return token.content || '';
            } else if (token.type === 'hardbreak') {
                return '';
            }
        });
        return cells.map(cell => cell.trim());
    });

    // ... (rest of the original function)
    return dataRows.map(row => headers.map((header, index) => row[index] || ''));
}
// End of the code context
describe('parseMarkdownTable', () => {
    test('should correctly parse a standard table', () => {
        const mdTable = `
        | Header 1 | Header 2 | Header 3 |
        |----------|----------|----------|
        | Row1Col1 | Row1Col2 | Row1Col3 |
        | Row2Col1 | Row2Col2 | Row2Col3 |
        `;
        const expected = [
            ['Header 1', 'Header 2', 'Header 3'],
            ['Row1Col1', 'Row1Col2', 'Row1Col3'],
            ['Row2Col1', 'Row2Col2', 'Row2Col3']
        ];
        const result = parseMarkdownTable(mdTable);
        expect(result).toEqual(expected);
    });

    test('should correctly parse a table with inconsistent columns', () => {
        const mdTable = `
        | Header 1 | Header 2 |
        |----------|----------|
        | Row1     | Row1Col2 | ExtraCol |
        | Row2     |
        `;
        const expected = [
            ['Header 1', 'Header 2'],
            ['Row1', 'Row1Col2', 'ExtraCol'],
            ['Row2']
        ];
        const result = parseMarkdownTable(mdTable);
        expect(result).toEqual(expected);
    });

    test('should correctly parse a table with empty cells', () => {
        const mdTable = `
        | Header 1 | Header 2 | Header 3 |
        |----------|----------|----------|
        |          | Row1Col2 |          |
        | Row2Col1 |          | Row2Col3 |
        `;
        const expected = [
            ['Header 1', 'Header 2', 'Header 3'],
            ['', 'Row1Col2', ''],
            ['Row2Col1', '', 'Row2Col3']
        ];
        const result = parseMarkdownTable(mdTable);
        expect(result).toEqual(expected);
    });

    test('should correctly parse a table with all empty rows', () => {
        const mdTable = `
        | Header 1 | Header 2 | Header 3 |
        |----------|----------|----------|
        |          |          |          |
        |          |          |          |
        `;
        const expected = [
            ['Header 1', 'Header 2', 'Header 3'],
            ['', '', ''],
            ['', '', '']
        ];
        const result = parseMarkdownTable(mdTable);
        expect(result).toEqual(expected);
    });

    test('should correctly parse a table with excessive whitespace', () => {
        const mdTable = `
        |  Header 1  |  Header 2  |  Header 3  |
        |------------|------------|------------|
        |  Row1Col1  |  Row1Col2  |  Row1Col3  |
        |  Row2Col1  |  Row2Col2  |  Row2Col3  |
        `;
        const expected = [
            ['Header 1', 'Header 2', 'Header 3'],
            ['Row1Col1', 'Row1Col2', 'Row1Col3'],
            ['Row2Col1', 'Row2Col2', 'Row2Col3']
        ];
        const result = parseMarkdownTable(mdTable);
        expect(result).toEqual(expected);
    });
});
