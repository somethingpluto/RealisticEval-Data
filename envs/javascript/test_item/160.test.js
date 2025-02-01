/**
 * Compresses long filenames to the specified maximum length by inserting an ellipsis in the middle while preserving the filename extension, which defaults to 18 characters
 * For example:
 *      compressFilename('verylongfilename.txt', 10) output: verylongfi***.txt
 *
 * @param {string} fileName - The original file name to be compressed.
 * @param {number} maxLength - The maximum allowed length for the compressed file name. Defaults to 18.
 * @returns {string} The compressed file name, with the middle section replaced by ellipses ('...'), or the original file name if it is within the maximum length.
 */
function compressFileName(fileName, maxLength = 18) {
    const extensionIndex = fileName.lastIndexOf('.');
    const nameLength = extensionIndex > -1 ? extensionIndex : fileName.length;
    const namePart = fileName.substring(0, nameLength);
    const extPart = extensionIndex > -1 ? fileName.substring(extensionIndex) : '';

    if (nameLength <= maxLength) {
        return fileName;
    }

    const namePartLength = maxLength - extPart.length;
    const ellipsisLength = 3;
    const startPartLength = Math.floor((namePartLength - ellipsisLength) / 2);
    const endPartLength = namePartLength - startPartLength - ellipsisLength;

    const compressedName = namePart.substring(0, startPartLength) + '***' + namePart.substring(namePart.length - endPartLength);
    return compressedName + extPart;
}
describe('compressFilename', () => {
    test('should return the filename unchanged if under max length', () => {
        expect(compressFilename('file.txt', 10)).toBe('file.txt');
    });

    test('should truncate and append *** if filename exceeds max length', () => {
        expect(compressFilename('verylongfilename.txt', 10)).toBe('verylongfi***.txt');
    });

    test('should preserve file extension after compression', () => {
        expect(compressFilename('document.pdf', 5)).toBe('docum***.pdf');
    });

    test('should truncate and append *** if filename exceeds', () => {
        expect(compressFilename('short.mp3', 2)).toBe('sh***.mp3');
    });
});
