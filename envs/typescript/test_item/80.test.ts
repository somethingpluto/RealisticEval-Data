// ... (previous code for context)
import { sanitizeFilename } from './sanitizeFilename';

// Unit tests for sanitizeFilename function
describe('sanitizeFilename', () => {
  it('should remove illegal characters from a Windows file path string', () => {
    expect(sanitizeFilename('file?name.txt')).toBe('filename.txt');
    expect(sanitizeFilename('C:\\path\\to\\file*name.txt')).toBe('C:\\path\\to\\filename.txt');
    expect(sanitizeFilename('another\\file?name.txt')).toBe('another\\filename.txt');
    // Add more test cases as needed
  });
});
// ... (continuation of code)
describe('TestSanitizeFilename', () => {
    describe('test_valid_filename', () => {
        it('should handle valid filenames correctly', () => {
            expect(sanitizeFilename("valid_filename.txt")).toBe("valid_filename.txt");
        });
    });

    describe('test_illegal_characters', () => {
        it('should sanitize filenames with illegal characters', () => {
            expect(sanitizeFilename("invalid<filename>.txt")).toBe("invalid_filename_.txt");
            expect(sanitizeFilename("file/name:with*illegal|chars?.txt")).toBe("file_name_with_illegal_chars_.txt");
        });
    });

    describe('test_long_filename', () => {
        it('should truncate long filenames to 255 characters', () => {
            const longFilename = "a".repeat(300) + ".txt";
            const sanitizedFilename = sanitizeFilename(longFilename);
            expect(sanitizedFilename.length).toBe(255);
            expect(sanitizedFilename).toBe("a".repeat(255));
        });
    });

    describe('test_empty_filename', () => {
        it('should handle empty filenames correctly', () => {
            expect(sanitizeFilename("")).toBe("");
        });
    });
});
