// Additions at the start of the file
import { parse } from 'path';

/**
 * Extracts the file extension from a given file name.
 * If the file name does not contain an extension, returns an empty string.
 * If the file name is invalid, throws an error.
 *
 * @param {string} fileName - The full name of the file.
 * @returns {string} The file extension without the dot.
 * @throws Will throw an error if the file name is invalid.
 */
function getFileExtension(fileName: string): string {
  // Validate the file name
  if (!fileName || typeof fileName !== 'string') {
    throw new Error('Invalid file name');
  }

  // Use path.parse to extract the extension
  const { ext } = parse(fileName);
  if (!ext) {
    throw new Error('No file extension found');
  }

  return ext.substring(1); // Remove the dot
}

// Example usage:
try {
  console.log(getFileExtension('example.txt')); // Output: txt
  console.log(getFileExtension('example')); // This will throw an error
} catch (error) {
  console.error(error.message);
}
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
