/**
 * Remove illegal characters from a Windows file path string.
 *
 * @param {string} filename - The original filename string to be sanitized.
 * @returns {string} A sanitized string that is safe to use as a Windows filename.
 */
function sanitizeFilename(filename) {
    // Define illegal characters for Windows filenames
    const illegalChars = /[<>:"\/\\|?*\x00-\x1F]/g;
    
    // Replace illegal characters with an empty string
    return filename.replace(illegalChars, '');
}
describe('TestSanitizeFilename', () => {
    it('should handle valid filenames correctly', () => {
        expect(sanitizeFilename("valid_filename.txt")).toBe("valid_filename.txt");
    });

    it('should sanitize filenames with illegal characters', () => {
        expect(sanitizeFilename("invalid<filename>.txt")).toBe("invalid_filename_.txt");
        expect(sanitizeFilename("file/name:with*illegal|chars?.txt")).toBe("file_name_with_illegal_chars_.txt");
    });

    it('should truncate long filenames to 255 characters', () => {
        const longFilename = "a".repeat(300) + ".txt";
        const sanitizedFilename = sanitizeFilename(longFilename);
        expect(sanitizedFilename.length).toBe(255);
        expect(sanitizedFilename).toBe("a".repeat(255));
    });

    it('should handle empty filenames correctly', () => {
        expect(sanitizeFilename("")).toBe("");
    });
});
