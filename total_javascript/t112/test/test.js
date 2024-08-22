describe('htmlToMDSyntax', () => {
    test('should convert basic HTML tags to Markdown syntax', () => {
        const html = '<h1>Title</h1><p>Paragraph</p><code>code snippet</code>';
        const expected = '# Title\nParagraph\n`code snippet`';
        const result = htmlToMDSyntax(html);
        expect(result).toBe(expected);
    });

    test('should convert ordered list to Markdown syntax', () => {
        const html = '<ol><li>First</li><li>Second</li><li>Third</li></ol>';
        const expected = '1. First\n2. Second\n3. Third';
        const result = htmlToMDSyntax(html);
        expect(result).toBe(expected);
    });

    test('should convert unordered list to Markdown syntax', () => {
        const html = '<ul><li>First</li><li>Second</li><li>Third</li></ul>';
        const expected = '- First\n- Second\n- Third';
        const result = htmlToMDSyntax(html);
        expect(result).toBe(expected);
    });

    test('should handle nested lists correctly such as an ordered list containing an unordered sublist', () => {
        const html = '<ol><li>First<ul><li>Sub First</li></ul></li><li>Second</li></ol>';
        const expected = '1. First\n- Sub First\n\n\n2. Second';
        const result = htmlToMDSyntax(html);
        expect(result).toBe(expected);
    });

    test('should handle mixed content with headings and lists', () => {
        const html = '<h2>Subheading</h2><p>Some text</p><ul><li>Item</li></ul>';
        const expected = '## Subheading\nSome text\n\n- Item';
        const result = htmlToMDSyntax(html);
        expect(result).toBe(expected);
    });
});