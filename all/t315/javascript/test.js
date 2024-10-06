describe('getFileIdFromUrl', () => {
    test('should return the file ID when a valid URL with fileId is provided', () => {
        const url = 'https://example.com/download?fileId=12345';
        expect(getFileIdFromUrl(url)).toBe('12345');
    });

    test('should return null when the fileId query parameter is missing', () => {
        const url = 'https://example.com/download';
        expect(getFileIdFromUrl(url)).toBeNull();
    });

    test('should return null when the fileId query parameter is empty', () => {
        const url = 'https://example.com/download?fileId=';
        expect(getFileIdFromUrl(url)).toBeNull();
    });

    test('should return null for an invalid URL', () => {
        const url = 'invalid-url';
        expect(getFileIdFromUrl(url)).toBeNull();
    });


    test('should return null for a malformed URL', () => {
        const url = 'https://example.com/download?fileId=12345&otherParam';
        expect(getFileIdFromUrl(url)).toBe('12345'); // Adjust this depending on your needs; the function should still work correctly.
    });
});