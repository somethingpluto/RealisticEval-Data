describe('parseMarkdownTable', () => {
    test('Standard table', () => {
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

    test('Inconsistent columns', () => {
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

    test('Empty cells', () => {
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

    test('All empty rows', () => {
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

    test('Excessive whitespace', () => {
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