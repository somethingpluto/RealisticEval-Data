import { Buffer } from 'buffer';

/**
 * Converts a string to Base64 encoding.
 *
 * @param {string} input - The string to be converted to Base64.
 * @returns {string} The Base64 encoded string.
 */
function convertToBase64(input: string): string {
    return Buffer.from(input).toString('base64');
}
describe('Base64 Encoding Tests', () => {
    test('Convert simple string to Base64', () => {
        expect(convertToBase64("Hello, World!")).toBe("SGVsbG8sIFdvcmxkIQ==");
    });

    test('Convert empty string to Base64', () => {
        expect(convertToBase64("")).toBe("");
    });

    test('Convert string with spaces to Base64', () => {
        expect(convertToBase64("Test String with Spaces")).toBe("VGVzdCBTdHJpbmcgd2l0aCBTcGFjZXM=");
    });

    test('Convert string with special characters to Base64', () => {
        expect(convertToBase64("Special characters: @#&*()")).toBe("U3BlY2lhbCBjaGFyYWN0ZXJzOiBAIyYqKCk=");
    });

    test('Convert string with non-ASCII characters to Base64', () => {
        expect(convertToBase64("你好，世界！")).toBe("5L2g5aW977yM5LiW55WM77yB");
    });

    test('Convert long string to Base64', () => {
        const longString: string = "This is a very long string that exceeds normal lengths for testing purposes.";
        expect(convertToBase64(longString)).toBe("VGhpcyBpcyBhIHZlcnkgbG9uZyBzdHJpbmcgdGhhdCBleGNlZWRzIG5vcm1hbCBsZW5ndGhzIGZvciB0ZXN0aW5nIHB1cnBvc2VzLg==");
    });
});
