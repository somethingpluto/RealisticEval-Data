import { describe, it, expect } from '@jest/globals';

describe('formatComment', () => {
    it('should format a simple string', () => {
        const input = "This is a very long string that needs to be formatted into multiple lines with comments.";
        const expectedOutput = `# This is a very long string that needs to
# be formatted into multiple lines with
# comments.`;

        expect(formatComment(input)).toBe(expectedOutput);
    });

    it('should handle empty strings', () => {
        const input = "";
        const expectedOutput = "";

        expect(formatComment(input)).toBe(expectedOutput);
    });

    it('should respect the maximum line length', () => {
        const input = "This is a very long string that needs to be formatted into multiple lines with comments.";
        const maxLength = 30;
        const expectedOutput = `# This is a very long string
# that needs to be formatted
# into multiple lines with
# comments.`;

        expect(formatComment(input, maxLength)).toBe(expectedOutput);
    });

    it('should handle strings shorter than max length', () => {
        const input = "Short string";
        const maxLength = 50;
        const expectedOutput = `# Short string`;

        expect(formatComment(input, maxLength)).toBe(expectedOutput);
    });

    it('should handle strings exactly at max length', () => {
        const input = "Exactly sixty characters";
        const maxLength = 60;
        const expectedOutput = `# Exactly sixty characters`;

        expect(formatComment(input, maxLength)).toBe(expectedOutput);
    });

    it('should handle strings ending with spaces', () => {
        const input = "String with trailing spaces     ";
        const expectedOutput = `# String with trailing spaces`;

        expect(formatComment(input)).toBe(expectedOutput);
    });

    it('should handle strings with spaces at max length', () => {
        const input = "This is a string with a space at the end of the line   ";
        const maxLength = 35;
        const expectedOutput = `# This is a string with a space at
# the end of the line`;

        expect(formatComment(input, maxLength)).toBe(expectedOutput);
    });
});
