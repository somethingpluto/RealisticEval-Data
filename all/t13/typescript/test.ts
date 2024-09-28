import { parseMarkdownTable } from './your-module';
import { describe, it, expect } from '@jest/globals';

describe('parseMarkdownTable', () => {
    it('should parse a standard table', () => {
        const mdTable = `
        | Header 1 | Header 2 | Header 3 |
        |----------|----------|----------|
        | Row1Col1 | Row1Col2 | Row1Col3 |
        | Row2Col1 | Row2Col2 | Row2Col3 |
        `;
        const expected: Array<[string, ...string[]]> = [
            ['Header 1', 'Header 2', 'Header 3'],
            ['Row1Col1', 'Row1Col2', 'Row1Col3'],
            ['Row2Col1', 'Row2Col2', 'Row2Col3']
        ];
        const result = parseMarkdownTable(mdTable);
        expect(result).toEqual(expected);
    });

    it('should handle inconsistent columns', () => {
        const mdTable = `
        | Header 1 | Header 2 |
        |----------|----------|
        | Row1     | Row1Col2 | ExtraCol |
        | Row2     |
        `;
        const expected: Array<[string, ...string[]]> = [
            ['Header 1', 'Header 2'],
            ['Row1', 'Row1Col2', 'ExtraCol'],
            ['Row2']
        ];
        const result = parseMarkdownTable(mdTable);
        expect(result).toEqual(expected);
    });

    it('should handle empty cells', () => {
        const mdTable = `
        | Header 1 | Header 2 | Header 3 |
        |----------|----------|----------|
        |          | Row1Col2 |          |
        | Row2Col1 |          | Row2Col3 |
        `;
        const expected: Array<[string, ...string[]]> = [
            ['Header 1', 'Header 2', 'Header 3'],
            ['', 'Row1Col2', ''],
            ['Row2Col1', '', 'Row2Col3']
        ];
        const result = parseMarkdownTable(mdTable);
        expect(result).toEqual(expected);
    });

    it('should handle all empty rows', () => {
        const mdTable = `
        | Header 1 | Header 2 | Header 3 |
        |----------|----------|----------|
        |          |          |          |
        |          |          |          |
        `;
        const expected: Array<[string, ...string[]]> = [
            ['Header 1', 'Header 2', 'Header 3'],
            ['', '', ''],
            ['', '', '']
        ];
        const result = parseMarkdownTable(mdTable);
        expect(result).toEqual(expected);
    });

    it('should handle excessive whitespace', () => {
        const mdTable = `
        |  Header 1  |  Header 2  |  Header 3  |
        |------------|------------|------------|
        |  Row1Col1  |  Row1Col2  |  Row1Col3  |
        |  Row2Col1  |  Row2Col2  |  Row2Col3  |
        `;
        const expected: Array<[string, ...string[]]> = [
            ['Header 1', 'Header 2', 'Header 3'],
            ['Row1Col1', 'Row1Col2', 'Row1Col3'],
            ['Row2Col1', 'Row2Col2', 'Row2Col3']
        ];
        const result = parseMarkdownTable(mdTable);
        expect(result).toEqual(expected);
    });
});