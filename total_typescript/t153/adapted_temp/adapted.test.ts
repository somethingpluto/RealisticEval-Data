// @ts-ignore
const crypto = require('crypto');

describe('compressHash', () => {

    test('should return a string of length 5', () => {
        // @ts-ignore
        const hash = crypto.createHash('sha256').update('test').digest();
        // @ts-ignore
        const result = compressHash(hash);
        expect(result.length).toBe(5);
    });

    test('should return different strings for different inputs', () => {
        // @ts-ignore
        const hash1 = crypto.createHash('sha256').update('test1').digest();
        // @ts-ignore
        const hash2 = crypto.createHash('sha256').update('test2').digest();
        // @ts-ignore
        const result1 = compressHash(hash1);
        // @ts-ignore
        const result2 = compressHash(hash2);
        expect(result1).not.toBe(result2);
    });

    test('should return a consistent result for the same input', () => {
        // @ts-ignore
        const hash = crypto.createHash('sha256').update('test').digest();
        // @ts-ignore
        const result1 = compressHash(hash);
        // @ts-ignore
        const result2 = compressHash(hash);
        expect(result1).toBe(result2);
    });

    test('should handle a hash of all zeros', () => {
        const hash = Buffer.alloc(32, 0); // 32 bytes of zeros
        // @ts-ignore
        const result = compressHash(hash);
        expect(result).toMatch(/^[0-9a-zA-Z]{5}$/);
    });

    test('should handle a hash of all ones', () => {
        const hash = Buffer.alloc(32, 255); // 32 bytes of 0xFF (255 in decimal)
        // @ts-ignore
        const result = compressHash(hash);
        expect(result).toMatch(/^[0-9a-zA-Z]{5}$/);
    });
});

/**
 * The input hash buffer is compressed into a number letter string of length no less than 5
 *
 * @param {Buffer} hash - The hash buffer to be compressed.
 * @returns {string} A compressed string representation of the hash.
 */
function compressHash(hash: Buffer): string {
    // Convert the hash buffer to a number in base 16 (hexadecimal)
    let num = parseInt(hash.toString("hex"), 16);

    // Define the base and alphabet for encoding
    const base = 62;
    const alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // Initialize the result string
    let result = "";

    // Convert the number to the desired base (base 62) and construct the compressed string
    while (result.length < 5) {
        const remainder = num % base;
        result += alphabet.charAt(remainder);
        num = Math.floor(num / base);
    }

    return result;
}