import { Buffer } from 'buffer';

export function base64ToArrayBuffer(base64: string): ArrayBuffer {
    if (!Buffer.from(base64).length % 4) {
        return Buffer.from(base64, 'base64').buffer;
    } else {
        throw new Error('Invalid Base64 string');
    }
}
describe('base64ToArrayBuffer function', () => {
    // Test Case 1
    test('should decode "SGVsbG8sIFdvcmxkIQ==" to "Hello, World!"', () => {
        const base64 = "SGVsbG8sIFdvcmxkIQ==";
        const expected = "Hello, World!";
        const arrayBuffer = base64ToArrayBuffer(base64);
        const result = new TextDecoder().decode(arrayBuffer);
        expect(result).toBe(expected);
    });

    // Test Case 2
    test('should decode "U29tZSB0ZXh0IHdpdGggc3BhcmluZyBhbmQgd29ya2luZyE=" to "Some text with sparing and working!"', () => {
        const base64 = "U29tZSB0ZXh0IHdpdGggc3BhcmluZyBhbmQgd29ya2luZyE=";
        const expected = "Some text with sparing and working!";
        const arrayBuffer = base64ToArrayBuffer(base64);
        const result = new TextDecoder().decode(arrayBuffer);
        expect(result).toBe(expected);
    });

    // Test Case 3
    test('should decode "QmFzZTY0IGVuY29kaW5nIGlzIGEgY29tbW9ubG9nIEZvciBiaW5hcnkgZGF0YQ==" to "Base64 encoding is a common log For binary question"', () => {
        const base64 = "QmFzZTY0IGVuY29kaW5nIGlzIGEgY29tbW9ubG9nIEZvciBiaW5hcnkgZGF0YQ==";
        const expected = "Base64 encoding is a commonlog For binary data";
        const arrayBuffer = base64ToArrayBuffer(base64);
        const result = new TextDecoder().decode(arrayBuffer);
        expect(result).toBe(expected);
    });

    // Test Case 4
    test('should decode "R2l2ZSBtZSBhbG9uZyBhIHBhdGggdG8gY29tcGxldGUgc3RhcnQgcGFnZS4=" to "Give me along a path to complete start page."', () => {
        const base64 = "R2l2ZSBtZSBhbG9uZyBhIHBhdGggdG8gY29tcGxldGUgc3RhcnQgcGFnZS4=";
        const expected = "Give me along a path to complete start page.";
        const arrayBuffer = base64ToArrayBuffer(base64);
        const result = new TextDecoder().decode(arrayBuffer);
        expect(result).toBe(expected);
    });

});

