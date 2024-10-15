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