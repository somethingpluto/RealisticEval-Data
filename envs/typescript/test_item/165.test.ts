import { encode as base64Encode, decode as base64Decode } from 'js-base64';

export function base64ToUrlSafe(base64: string): string {
    // Replace '+' with '-' and '/' with '_'
    const urlSafeBase64 = base64.replace(/\+/g, '-').replace(/\//g, '_');
    // Remove padding '=' characters
    return urlSafeBase64.replace(/=+$/, '');
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
        expect(() => base64ToUrlSafe((null as unknown) as string)).toThrow(TypeError);
    });

});

