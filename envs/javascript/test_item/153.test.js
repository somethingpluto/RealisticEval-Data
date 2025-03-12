/**
 * The input hash buffer is compressed into a number letter string of length no less than 5
 *
 * @param {Buffer} hash - The hash buffer to be compressed.
 * @returns {string} A compressed string representation of the hash.
 */
function compressHash(hash) {
    const base64Chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
    let compressedString = '';
    let bitBuffer = 0;
    let bitCount = 0;

    for (let i = 0; i < hash.length; i++) {
        bitBuffer = (bitBuffer << 8) | hash[i];
        bitCount += 8;

        while (bitCount >= 6) {
            bitCount -= 6;
            const index = (bitBuffer >>> bitCount) & 0x3F;
            compressedString += base64Chars[index];
        }
    }

    if (bitCount > 0) {
        const index = (bitBuffer << (6 - bitCount)) & 0x3F;
        compressedString += base64Chars[index];
    }

    // Ensure the compressed string is at least 5 characters long
    while (compressedString.length < 5) {
        compressedString += base64Chars[0];
    }

    return compressedString;
}
describe('compressHash', () => {

    test('should return a string of length 5', () => {
        const hash = crypto.createHash('sha256').update('test').digest();
        const result = compressHash(hash);
        expect(result.length).toBe(5);
    });

    test('should return different strings for different inputs', () => {
        const hash1 = crypto.createHash('sha256').update('test1').digest();
        const hash2 = crypto.createHash('sha256').update('test2').digest();
        const result1 = compressHash(hash1);
        const result2 = compressHash(hash2);
        expect(result1).not.toBe(result2);
    });

    test('should return a consistent result for the same input', () => {
        const hash = crypto.createHash('sha256').update('test').digest();
        const result1 = compressHash(hash);
        const result2 = compressHash(hash);
        expect(result1).toBe(result2);
    });

    test('should handle a hash of all zeros', () => {
        const hash = Buffer.alloc(32, 0); // 32 bytes of zeros
        const result = compressHash(hash);
        expect(result).toMatch(/^[0-9a-zA-Z]{5}$/);
    });

    test('should handle a hash of all ones', () => {
        const hash = Buffer.alloc(32, 255); // 32 bytes of 0xFF (255 in decimal)
        const result = compressHash(hash);
        expect(result).toMatch(/^[0-9a-zA-Z]{5}$/);
    });
});
