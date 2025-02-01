/**
 * The Uint8 array is converted into 4 Base64 characters as a group of 3 bytes for processing, and the output of less than 3 is filled with =, and the resulting Base64 string is returned
 *
 * @param {Uint8Array} uint8Array - The Uint8Array to be converted.
 * @returns {string} - The resulting Base64-encoded string.
 */
function uint8ArrayToBase64(uint8Array) {
    const base64Chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
    let base64String = '';

    for (let i = 0; i < uint8Array.length; i += 3) {
        const chunk = uint8Array.slice(i, i + 3);
        const chunkBits = chunk.reduce((acc, byte, index) => acc + (byte << (8 * index)), 0);
        const base64Chunk = [
            (chunkBits >> 18) & 0x3F,
            (chunkBits >> 12) & 0x3F,
            (chunkBits >> 6) & 0x3F,
            chunkBits & 0x3F
        ].map(code => base64Chars[code]).join('');

        base64String += base64Chunk;
    }

    const padding = (uint8Array.length % 3) ? (3 - uint8Array.length % 3) : 0;
    base64String += '='.repeat(padding);

    return base64String;
}
describe('uint8ArrayToBase64', () => {
    test('should convert an empty Uint8Array', () => {
        const uint8Array = new Uint8Array([]);
        const result = uint8ArrayToBase64(uint8Array);
        expect(result).toBe('');
    });

    test('should convert a Uint8Array with one byte', () => {
        const uint8Array = new Uint8Array([255]);
        const result = uint8ArrayToBase64(uint8Array);
        expect(result).toBe('/w==');
    });

    test('should convert a Uint8Array with two bytes', () => {
        const uint8Array = new Uint8Array([255, 255]);
        const result = uint8ArrayToBase64(uint8Array);
        expect(result).toBe('//8=');
    });

    test('should convert a Uint8Array with three bytes', () => {
        const uint8Array = new Uint8Array([255, 255, 255]);
        const result = uint8ArrayToBase64(uint8Array);
        expect(result).toBe('////');
    });

    test('should convert a Uint8Array with four bytes', () => {
        const uint8Array = new Uint8Array([72, 101, 108, 108]);
        const result = uint8ArrayToBase64(uint8Array);
        expect(result).toBe('SGVsbA==');
    });
});
