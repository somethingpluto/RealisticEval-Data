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