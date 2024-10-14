const compressWhitespace = require('./compressWhitespace');

describe('compressWhitespace', () => {
    it('should handle empty strings correctly', () => {
        expect(compressWhitespace('')).toBe('');
    });

    it('should handle strings without extra whitespace', () => {
        expect(compressWhitespace('hello world')).toBe('hello world');
    });

    it('should handle strings with leading and trailing whitespace', () => {
        expect(compressWhitespace('  hello world  ')).toBe('hello world');
    });

    it('should handle strings with multiple consecutive spaces', () => {
        expect(compressWhitespace('hello   world')).toBe('hello world');
    });

    it('should handle strings with tabs and newlines', () => {
        expect(compressWhitespace('hello\t\tworld\n')).toBe('hello world');
    });
});

// Ensure to run the tests with Jest
// npx jest