describe('getFileExtension', () => {
    test('should return the file extension for a standard file', () => {
        // @ts-ignore
        expect(getFileExtension('example.txt')).toBe('txt');
    });

    test('should return an empty string for files without an extension', () => {
        // @ts-ignore
        expect(getFileExtension('example')).toBe('');
    });

    test('should handle files with multiple dots', () => {
        // @ts-ignore
        expect(getFileExtension('example.with.many.dots.jpg')).toBe('jpg');
    });

    test('should return an empty string for filenames that end with a dot', () => {
        // @ts-ignore
        expect(getFileExtension('example.')).toBe('');
    });

    test('should correctly handle case sensitivity', () => {
        // @ts-ignore
        expect(getFileExtension('example.JPG')).toBe('JPG');
    });
});
/**
 * Extract the file extension and return it if it exists. If not, an empty string is returned
 *
 * @param {string} file_name - The full name of the file from which to extract the extension.
 * @returns {string} The file extension without the dot, or an empty string if no extension is found.
 */
export function getFileExtension(file_name: string): string {
    // Regex to match the portion after the last dot in the filename
    const regex = /(?:\.([^.]+))?$/;
    const match = regex.exec(file_name);

    // Return the captured group (extension) if it exists
    if (match && match[1]) {
        return match[1];
    }

    // Return an empty string if no extension is found
    return '';
}
