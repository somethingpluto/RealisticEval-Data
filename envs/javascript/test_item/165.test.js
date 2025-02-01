/**
 * Converts a standard Base64 encoded string into a URL-safe Base64 encoded string.
 *
 * @param {string} base64 - The standard Base64 encoded string to be converted.
 * @returns {string} The URL-safe Base64 encoded string.
 */
export function base64ToUrlSafe(base64) {
    return base64.replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}
describe('base64ToUrlSafe', () => {

    test('should correctly convert a standard Base64 string to URL-safe format', () => {
        const base64 = "YW55IGNhcm5hbCBwbGVhc3VyZS4+/w==";
        const result = base64ToUrlSafe(base64);
        expect(result).toBe("YW55IGNhcm5hbCBwbGVhc3VyZS4-_w");
    });

    test('should return an empty string when the input is an empty string', () => {
        const base64 = "";
        const result = base64ToUrlSafe(base64);
        expect(result).toBe("");
    });

    test('should remove only the trailing "=" characters', () => {
        const base64 = "dGVzdA==";
        const result = base64ToUrlSafe(base64);
        expect(result).toBe("dGVzdA");
    });

    test('should handle strings without any characters that need replacement', () => {
        const base64 = "dGVzdA";
        const result = base64ToUrlSafe(base64);
        expect(result).toBe("dGVzdA");
    });

    test('should handle a base64 string with multiple "+" and "/" characters', () => {
        const base64 = "aGVsbG8rL3dvcmxkLw==";
        const result = base64ToUrlSafe(base64);
        expect(result).toBe("aGVsbG8rL3dvcmxkLw");
    });

    test('should throw an error when input is not a string', () => {
        expect(() => base64ToUrlSafe(null)).toThrow(TypeError);
    });

});
