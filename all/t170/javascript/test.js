describe('HTML to Markdown Converter', () => {
  
    test('testSimpleLineBreak', () => {
        const input = 'Hello<br>World';
        const expectedOutput = 'Hello\nWorld';
        expect(convert(input)).toBe(expectedOutput);
    });

    test('testStrongTags', () => {
        const input = 'This is <strong>important</strong> text.';
        const expectedOutput = 'This is **important** text.';
        expect(convert(input)).toBe(expectedOutput);
    });

    test('testEmphasisTags', () => {
        const input = 'This is <em>emphasized</em> text.';
        const expectedOutput = 'This is *emphasized* text.';
        expect(convert(input)).toBe(expectedOutput);
    });

    test('testUnorderedList', () => {
        const input = '<ul><li>Item 1</li><li>Item 2</li></ul>';
        const expectedOutput = '* Item 1\n* Item 2\n';
        expect(convert(input)).toBe(expectedOutput);
    });

    test('testAnchorTags', () => {
        const input = 'Check this link: <a href="http://example.com">Example</a>.';
        const expectedOutput = 'Check this link: [Example](http://example.com).';
        expect(convert(input)).toBe(expectedOutput);
    });
});