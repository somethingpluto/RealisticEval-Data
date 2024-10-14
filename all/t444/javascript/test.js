const formatComment = require('./path/to/formatComment'); // Adjust the path accordingly

describe('formatComment', () => {
    it('should format a short comment correctly', () => {
        const input = 'This is a short comment.';
        const expectedOutput = '# This is a short comment.';
        expect(formatComment(input)).toBe(expectedOutput);
    });

    it('should format a long comment correctly', () => {
        const input = 'This is a very long comment that needs to be broken down into multiple lines to fit within the specified maximum length.';
        const expectedOutput = `# This is a very long comment that needs to be broken
# down into multiple lines to fit within the specified
# maximum length.`;
        expect(formatComment(input)).toBe(expectedOutput);
    });

    it('should format a comment with custom maxLength', () => {
        const input = 'This is a comment with a custom maximum length.';
        const maxLength = 30;
        const expectedOutput = `# This is a comment with
# a custom maximum length.`;
        expect(formatComment(input, maxLength)).toBe(expectedOutput);
    });

    it('should handle empty strings correctly', () => {
        const input = '';
        const expectedOutput = '';
        expect(formatComment(input)).toBe(expectedOutput);
    });

    it('should handle single-word strings correctly', () => {
        const input = 'Single';
        const expectedOutput = '# Single';
        expect(formatComment(input)).toBe(expectedOutput);
    });
});
