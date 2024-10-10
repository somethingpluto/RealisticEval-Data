describe('removeComments', () => {
    it('should remove single line comments', () => {
        const input = 'Hello, world! # This is a comment';
        const expectedOutput = 'Hello, world!';
        expect(removeComments(input)).toBe(expectedOutput);
    });

    it('should handle multiple lines without comments', () => {
        const input = 'Hello, world!\nThis is another line\nAnd yet another one';
        const expectedOutput = 'Hello, world!\nThis is another line\nAnd yet another one';
        expect(removeComments(input)).toBe(expectedOutput);
    });

    it('should handle multiple lines with comments', () => {
        const input = 'Hello, world!\n# This is a comment\nAnd yet another one\n# Another comment';
        const expectedOutput = 'Hello, world!\n\nAnd yet another one\n';
        expect(removeComments(input)).toBe(expectedOutput);
    });

    it('should handle empty string', () => {
        const input = '';
        const expectedOutput = '';
        expect(removeComments(input)).toBe(expectedOutput);
    });
});