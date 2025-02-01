/**
 * Extract the file extension and return it if it exists. If not, an empty string is returned
 *
 * @param {string} file_name - The full name of the file from which to extract the extension.
 * @returns {string} The file extension without the dot, or an empty string if no extension is found.
 */
function getFileExtension(file_name) {
    const extensionIndex = file_name.lastIndexOf('.');
    if (extensionIndex === -1) {
        return '';
    }
    return file_name.substring(extensionIndex + 1);
}
describe('getFileExtension', () => {
    test('should return the file extension for a standard file', () => {
        expect(getFileExtension('example.txt')).toBe('txt');
    });

    test('should return an empty string for files without an extension', () => {
        expect(getFileExtension('example')).toBe('');
    });

    test('should handle files with multiple dots', () => {
        expect(getFileExtension('example.with.many.dots.jpg')).toBe('jpg');
    });

    test('should return an empty string for filenames that end with a dot', () => {
        expect(getFileExtension('example.')).toBe('');
    });

    test('should correctly handle case sensitivity', () => {
        expect(getFileExtension('example.JPG')).toBe('JPG');
    });
});
