describe('htmlToPlainText', () => {
    test('converts a simple HTML string to plain text', () => {
        const htmlString = '<p>Hello, World!</p>';
        const result = htmlToPlainText(htmlString);
        expect(result).toBe('Hello, World!');
    });

    test('removes excess spaces between words', () => {
        const htmlString = '<p>This     is     a     test.</p>';
        const result = htmlToPlainText(htmlString);
        expect(result).toBe('This is a test.');
    });

    test('handles multiple paragraphs and removes excess line breaks', () => {
        const htmlString = '<p>First paragraph.</p>\n\n<p>Second paragraph.</p>';
        const result = htmlToPlainText(htmlString);
        expect(result).toBe('First paragraph.\nSecond paragraph.');
    });

    test('trims leading and trailing spaces', () => {
        const htmlString = '   <p>  Trimmed text.  </p>   ';
        const result = htmlToPlainText(htmlString);
        expect(result).toBe('Trimmed text.');
    });

    test('handles empty HTML string', () => {
        const htmlString = '';
        const result = htmlToPlainText(htmlString);
        expect(result).toBe('');
    });

    test('handles HTML with no text content', () => {
        const htmlString = '<div><span></span></div>';
        const result = htmlToPlainText(htmlString);
        expect(result).toBe('');
    });

    test('handles nested HTML elements', () => {
        const htmlString = '<div><p>Nested <strong>text</strong> here.</p></div>';
        const result = htmlToPlainText(htmlString);
        expect(result).toBe('Nested text here.');
    });

    test('correctly converts HTML with special characters', () => {
        const htmlString = '<p>Text with &amp; special characters.</p>';
        const result = htmlToPlainText(htmlString);
        expect(result).toBe('Text with & special characters.');
    });
});