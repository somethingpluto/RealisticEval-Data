describe('isBase64Image', () => {
    test('should return true for a valid PNG Base64 image string', () => {
        const validPng: string = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA';
        expect(isBase64Image(validPng)).toBe(true);
    });

    test('should return true for a valid JPEG Base64 image string', () => {
        const validJpeg: string = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAAAAAA';
        expect(isBase64Image(validJpeg)).toBe(true);
    });

    test('should return false for a string without the image data prefix', () => {
        const invalidFormat: string = 'data:text/plain;base64,SGVsbG8gd29ybGQ=';
        expect(isBase64Image(invalidFormat)).toBe(false);
    });

    test('should return false for a string with invalid Base64 characters', () => {
        const invalidBase64: string = 'data:image/png;base64,invalidBase64String@#%';
        expect(isBase64Image(invalidBase64)).toBe(false);
    });

    test('should return false for an empty string', () => {
        expect(isBase64Image('')).toBe(false);
    });

    test('should return false for a null input', () => {
        expect(isBase64Image(null as any)).toBe(false);
    });
});