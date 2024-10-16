describe('getFileExtension', () => {
    test('should return the file extension for a standard file', () => {
        expect(getFileExtension('example.txt')).toBe('txt');
    });

    test('should return an empty string for files without an extension', () => {
        expect(getFileExtension('example')).toBe('');
    });

    test('should handle files with multiple dots', () => {
        expect(getFileExtension('example.with.many.dots.jpg')).toBe('jpg');
    });

    test('should return an empty string for filenames that end with a dot', () => {
        expect(getFileExtension('example.')).toBe('');
    });

    test('should correctly handle case sensitivity', () => {
        expect(getFileExtension('example.JPG')).toBe('JPG');
    });
});