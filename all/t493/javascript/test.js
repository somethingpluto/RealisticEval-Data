describe('TestWrapContentGenerator', () => {
    it('test_empty_content', () => {
        /** Test with empty content. */
        const result = [...wrapContentGenerator("")];
        expect(result).toEqual([]);
    });

    it('test_single_line_content', () => {
        /** Test with a single line of content within default width. */
        const result = [...wrapContentGenerator("Hello, world!")];
        expect(result).toEqual(["Hello, world!"]);
    });

    it('test_multi_line_content', () => {
        /** Test with multiple lines of content each fitting within default width. */
        const content = "Hello\nWorld\nPython";
        const result = [...wrapContentGenerator(content)];
        expect(result).toEqual(["Hello", "World", "Python"]);
    });

    it('test_long_line', () => {
        /** Test with a single long line that exceeds the default width. */
        const content = "This is a very long line that should definitely be wrapped around the default width of 80 characters.";
        const result = [...wrapContentGenerator(content)];
        const longestLine = result.reduce((a, b) => a.length > b.length ? a : b, '');
        expect(longestLine.length).toBeLessThanOrEqual(80);
    });

    it('test_custom_width', () => {
        /** Test with a custom width. */
        const content = "This is a test for custom width setting.";
        const result = [...wrapContentGenerator(content, 10)];
        expect(result.every(line => line.length <= 10)).toBeTruthy();
    });

    it('test_only_whitespaces', () => {
        /** Test content that contains only whitespace characters. */
        const result = [...wrapContentGenerator("     ")];
        expect(result).toEqual(["\n"]);
    });
});