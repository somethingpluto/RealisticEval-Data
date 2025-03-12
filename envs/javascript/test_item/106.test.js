/**
 * Checks if the provided image data is a valid Base64 encoded image string.
 * 
 * @param {string} imageData - The image question string to be validated.
 * @returns {boolean} - Returns true if the imageData is a valid Base64 encoded image string, otherwise false.
 */
function isBase64Image(imageData) {
    // Regular expression to match a Base64 encoded image string
    const base64ImageRegex = /^data:image\/(png|jpg|jpeg|gif|bmp|webp);base64,([A-Za-z0-9+/=]+)$/;
    
    // Test the imageData against the regex
    return base64ImageRegex.test(imageData);
}
describe('isBase64Image', () => {
    test('should return true for a valid PNG Base64 image string', () => {
        const validPng = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA';
        expect(isBase64Image(validPng)).toBe(true);
    });

    test('should return true for a valid JPEG Base64 image string', () => {
        const validJpeg = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAAAAAA';
        expect(isBase64Image(validJpeg)).toBe(true);
    });

    test('should return false for a string without the image data prefix', () => {
        const invalidFormat = 'data:text/plain;base64,SGVsbG8gd29ybGQ=';
        expect(isBase64Image(invalidFormat)).toBe(false);
    });

    test('should return false for a string with invalid Base64 characters', () => {
        const invalidBase64 = 'data:image/png;base64,invalidBase64String@#%';
        expect(isBase64Image(invalidBase64)).toBe(false);
    });

    test('should return false for an empty string', () => {
        expect(isBase64Image('')).toBe(false);
    });

    test('should return false for a null input', () => {
        expect(isBase64Image(null)).toBe(false);
    });
});
