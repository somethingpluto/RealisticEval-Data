/**
 * Compresses long filenames to the specified maximum length by inserting an ellipsis in the middle while preserving the filename extension, which defaults to 18 characters.
 *
 * @param {string} fileName - The original file name to be compressed.
 * @param {number} maxLength - The maximum allowed length for the compressed file name. Defaults to 18.
 * @returns {string} The compressed file name, with the middle section replaced by ellipses ('...'), or the original file name if it is within the maximum length.
 */
function compressFileName(fileName, maxLength = 18) {
    // Check if the fileName is already within the maxLength
    if (fileName.length <= maxLength) {
        return fileName;
    }

    // Extract the file extension
    const lastDotIndex = fileName.lastIndexOf('.');
    const hasExtension = lastDotIndex !== -1;
    const extension = hasExtension ? fileName.substring(lastDotIndex) : '';
    const baseName = hasExtension ? fileName.substring(0, lastDotIndex) : fileName;

    // Calculate the length of the baseName that can be preserved
    const maxBaseLength = maxLength - extension.length;

    // Calculate the length of the parts before and after the ellipsis
    const partLength = Math.floor((maxBaseLength - 3) / 2); // 3 for the ellipsis

    // Construct the compressed filename
    const compressedBaseName = baseName.substring(0, partLength) + '...' + baseName.substring(baseName.length - partLength);

    return compressedBaseName + extension;
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
