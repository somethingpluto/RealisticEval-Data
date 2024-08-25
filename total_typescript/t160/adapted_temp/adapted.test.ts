describe('compressFileName', () => {
    test('returns the original file name if within maxLength', () => {
        // @ts-ignore
        expect(compressFileName('example.txt', 12)).toBe('example.txt');
    });

    test('compresses the file name correctly when it exceeds maxLength', () => {
        // @ts-ignore
        expect(compressFileName('longfilenameexample.txt', 18)).toBe('longf...xample.txt');
    });

    test('handles file names without extension correctly', () => {
        // @ts-ignore
        expect(compressFileName('averylongfilenamewithoutanextension', 20)).toBe('averylon...extension');
    });

    test('returns the original file name when maxLength is larger than file name', () => {
        // @ts-ignore
        expect(compressFileName('short.txt', 20)).toBe('short.txt');
    });

    test('compresses file names with special characters correctly', () => {
        // @ts-ignore
        expect(compressFileName('my$pecialfilename.txt', 18)).toBe('my$pe...lename.txt');
    });
});
/**
 * Compresses long filenames to the specified maximum length by inserting an ellipsis in the middle while preserving the filename extension, which defaults to 18 characters
 *
 * @param {string} fileName - The original file name to be compressed.
 * @param {number} maxLength - The maximum allowed length for the compressed file name. Defaults to 18.
 * @returns {string} The compressed file name, with the middle section replaced by ellipses ('...'), or the original file name if it is within the maximum length.
 */
export function compressFileName(
  fileName: string,
  maxLength: number = 18
): string {
  if (fileName.length <= maxLength) {
    return fileName.trim();
  }

  let extensionIndex = fileName.lastIndexOf('.');
  if (extensionIndex==-1) extensionIndex = fileName.length;
  const fileNameWithoutExtension = fileName.substring(0, extensionIndex);
  const fileExtension = fileName.substring(extensionIndex);

  const availableLength = maxLength - fileExtension.length - 3;
  const startLength = Math.floor(availableLength / 2);
  const endLength = availableLength - startLength;

  const compressedFileName =
    fileNameWithoutExtension.substring(0, startLength) +
    '...' +
    fileNameWithoutExtension.substring(fileNameWithoutExtension.length - endLength) +
    fileExtension;

  return compressedFileName;
}