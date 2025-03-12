// ... (previous code for context)
function uint8ArrayToBase64(uint8Array: Uint8Array): string {
    const base64Chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
    let base64 = '';
    let padding = 0;

    for (let i = 0; i < uint8Array.length; i += 3) {
        const byte1 = uint8Array[i];
        const byte2 = uint8Array[i + 1];
        const byte3 = uint8Array[i + 2];

        const index1 = byte1 >> 2;
        const index2 = ((byte1 & 3) << 4) | (byte2 >> 4);
        const index3 = ((byte2 & 15) << 2) | (byte3 >> 6);
        const index4 = byte3 & 63;

        base64 += base64Chars[index1] + base64Chars[index2] + base64Chars[index3] + (byte3 !== undefined ? base64Chars[index4] : '=');

        if (i + 3 >= uint8Array.length) {
            padding += 3 - (i + 3) % 3;
        }
    }

    return base64.substring(0, base64.length - padding) + '='.repeat(padding);
}
// ... (continuation of the code)
describe('uint8ArrayToBase64', () => {
    test('should convert an empty Uint8Array', () => {
        const uint8Array = new Uint8Array([]);
        // @ts-ignore
        const result = uint8ArrayToBase64(uint8Array);
        expect(result).toBe('');
    });

    test('should convert a Uint8Array with one byte', () => {
        const uint8Array = new Uint8Array([255]);
        // @ts-ignore
        const result = uint8ArrayToBase64(uint8Array);
        expect(result).toBe('/w==');
    });

    test('should convert a Uint8Array with two bytes', () => {
        const uint8Array = new Uint8Array([255, 255]);
        // @ts-ignore
        const result = uint8ArrayToBase64(uint8Array);
        expect(result).toBe('//8=');
    });

    test('should convert a Uint8Array with three bytes', () => {
        const uint8Array = new Uint8Array([255, 255, 255]);
        // @ts-ignore
        const result = uint8ArrayToBase64(uint8Array);
        expect(result).toBe('////');
    });

    test('should convert a Uint8Array with four bytes', () => {
        const uint8Array = new Uint8Array([72, 101, 108, 108]);
        // @ts-ignore
        const result = uint8ArrayToBase64(uint8Array);
        expect(result).toBe('SGVsbA==');
    });
});
