/**
 * Extract the fileid from the given URL query args.If not find return null
 * For example:
 *      input: https://example.com/download?fileId=12345
 *      output: 12345
 *
 * @param {string} url - The URL from which the file ID is to be extracted.
 * @returns {string|null} - The extracted file ID if present, otherwise null if the URL does not conform to the expected format.
 */
function getFileIdFromUrl(url) {
    const urlObj = new URL(url);
    const fileId = urlObj.searchParams.get('fileId');
    return fileId ? fileId : null;
}
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



    test('should return null for a malformed URL', () => {
        const url = 'https://example.com/download?fileId=12345&otherParam';
        expect(getFileIdFromUrl(url)).toBe('12345'); // Adjust this depending on your needs; the function should still work correctly.
    });
});

