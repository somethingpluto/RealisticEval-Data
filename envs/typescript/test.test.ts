/**
 * Compresses the filename before the extension, truncating it to a maximum length,
 * and replacing the excess with '***' if it exceeds the specified maximum length.
 *
 * @param {string} filename - The full filename with or without an extension.
 * @param {number} maxLength - The maximum allowed length of the filename before the extension.
 * @returns {string} The compressed filename with its extension preserved.
 *
 * @example
 * // returns "shortName.txt"
 * compressFilename("shortName.txt", 10);
 *
 * @example
 * // returns "longNa***.txt"
 * compressFilename("longNameFile.txt", 6);
 */
function compressFilename(filename: string, maxLength: number): string {
    // Extract the file extension
    const extensionMatch = filename.match(/\.[^\.]+$/);
    const extension = extensionMatch ? extensionMatch[0] : '';

    // Remove the extension from the filename for manipulation
    const basename = extension ? filename.slice(0, -extension.length) : filename;

    // Compress the basename if it's longer than maxLength
    const compressedBasename = basename.length > maxLength ?
        basename.slice(0, maxLength - 3) + '***' : basename;

    // Reattach the extension and return
    return compressedBasename + extension;
}
describe('compressFilename', () => {
    test('should return the filename unchanged if under max length', () => {
        expect(compressFilename('file.txt', 10)).toBe('file.txt');
    });

    test('should truncate and append *** if filename exceeds max length', () => {
        expect(compressFilename('verylongfilename.txt', 10)).toBe('verylon***.txt');
    });


    test('should preserve file extension after compression', () => {
        expect(compressFilename('docum***.pdf', 5)).toBe('docu***.pdf');
    });
    

    test('should return the original filename if max length is exactly the filename length', () => {
        expect(compressFilename('short.mp3', 9)).toBe('short.mp3');
    });

    test('should handle empty filenames and very short max lengths', () => {
        expect(compressFilename('', 3)).toBe('');
        expect(compressFilename('short.mp3', 3)).toBe('s***.mp3');
    });
});
