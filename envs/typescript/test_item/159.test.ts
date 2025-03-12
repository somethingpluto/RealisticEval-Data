import { sanitize } from 'sanitize-filename';

function removeFileExtension(file_name: string): string {
  const sanitizedFileName = sanitize(file_name);
  const dotIndex = sanitizedFileName.lastIndexOf('.');
  return dotIndex === -1 ? sanitizedFileName : sanitizedFileName.substring(0, dotIndex);
}
describe('removeFileExtension', () => {
    test('should remove the file extension from a standard file', () => {
        // @ts-ignore
        expect(removeFileExtension('document.txt')).toBe('document');
    });

    test('should return the original filename for files without an extension', () => {
        // @ts-ignore
        expect(removeFileExtension('document')).toBe('document');
    });

    test('should handle files with multiple dots correctly', () => {
        // @ts-ignore
        expect(removeFileExtension('my.file.with.many.extensions.pdf')).toBe('my.file.with.many.extensions');
    });

    test('should return the original filename if it ends with a dot', () => {
        // @ts-ignore
        expect(removeFileExtension('document.')).toBe('document');
    });

    test('should correctly handle filenames with dots in directory names', () => {
        // @ts-ignore
        expect(removeFileExtension('path.to/my.file.txt')).toBe('path.to/my.file');
    });
});
