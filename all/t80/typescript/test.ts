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