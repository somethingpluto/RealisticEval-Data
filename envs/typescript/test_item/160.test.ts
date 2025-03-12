import { sanitize } from 'sanitize-filename';

function compressFileName(fileName: string, maxLength: number = 18): string {
  const sanitizedFileName = sanitize(fileName);
  // ... rest of the function remains the same
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
