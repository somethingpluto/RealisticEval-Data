import { Buffer } from 'buffer';

function isBase64Image(imageData: string): boolean {
    // Check if the string starts with data:image and ends with ';base64,'
    if (!/^data:image\/[^\;]+;base64,/.test(imageData)) {
        return false;
    }

    // Decode the Base64 string and check if the resulting buffer is a valid image
    try {
        const buffer = Buffer.from(imageData.replace(/^data:image\/[^\;]+;base64,/, ''), 'base64');
        // Here you would typically check if the buffer contains valid image data
        // For example, by checking the image format or dimensions
        // This is a placeholder for such a check
        return true;
    } catch (error) {
        return false;
    }
}
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
