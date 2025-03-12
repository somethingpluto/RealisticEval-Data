/**
 * Removes the extension of the given filename and returns the remainder
 *
 * @param {string} file_name - The full name of the file from which to remove the extension.
 * @returns {string} The file name without the extension. If no extension is found, returns the original file name.
 */
function removeFileExtension(file_name) {
    // Find the last occurrence of the dot character
    const lastDotIndex = file_name.lastIndexOf('.');

    // If no dot is found or the dot is the first character, return the original file name
    if (lastDotIndex === -1 || lastDotIndex === 0) {
        return file_name;
    }

    // Return the substring from the start to the last dot index
    return file_name.substring(0, lastDotIndex);
}
describe('removeFileExtension', () => {
    test('should remove the file extension from a standard file', () => {
        expect(removeFileExtension('document.txt')).toBe('document');
    });

    test('should return the original filename for files without an extension', () => {
        expect(removeFileExtension('document')).toBe('document');
    });

    test('should handle files with multiple dots correctly', () => {
        expect(removeFileExtension('my.file.with.many.extensions.pdf')).toBe('my.file.with.many.extensions');
    });

    test('should return the original filename if it ends with a dot', () => {
        expect(removeFileExtension('document.')).toBe('document');
    });

    test('should correctly handle filenames with dots in directory names', () => {
        expect(removeFileExtension('path.to/my.file.txt')).toBe('path.to/my.file');
    });
});
