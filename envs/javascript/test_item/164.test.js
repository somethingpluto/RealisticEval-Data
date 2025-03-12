/**
 * The Uint8 array is converted into 4 Base64 characters as a group of 3 bytes for processing, and the output of less than 3 is filled with =, and the resulting Base64 string is returned
 *
 * @param {Uint8Array} uint8Array - The Uint8Array to be converted.
 * @returns {string} - The resulting Base64-encoded string.
 */
function uint8ArrayToBase64(uint8Array) {
    const base64Chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
    let result = '';
    let i = 0;

    while (i < uint8Array.length) {
        // First 6 bits of the first byte
        const byte1 = uint8Array[i++];
        const char1 = byte1 >> 2;

        // Last 2 bits of the first byte and first 4 bits of the second byte
        const byte2 = uint8Array[i++] || 0;
        const char2 = ((byte1 & 3) << 4) | (byte2 >> 4);

        // Last 4 bits of the second byte and first 2 bits of the third byte
        const byte3 = uint8Array[i++] || 0;
        const char3 = ((byte2 & 15) << 2) | (byte3 >> 6);

        // Last 6 bits of the third byte
        const char4 = byte3 & 63;

        result += base64Chars[char1] + base64Chars[char2] + base64Chars[char3] + base64Chars[char4];
    }

    // Add padding if necessary
    const paddingLength = (3 - (uint8Array.length % 3)) % 3;
    if (paddingLength > 0) {
        result = result.slice(0, result.length - paddingLength) + '=='.slice(0, paddingLength);
    }

    return result;
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
