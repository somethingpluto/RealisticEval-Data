describe('binaryStringToUint8Array', () => {
    test('should convert a full byte binary string', () => {
        const binaryStr = '11001010';
        // @ts-ignore
        const result = binaryStringToUint8Array(binaryStr);
        expect(result).toEqual(new Uint8Array([202]));
    });

    test('should convert multiple full byte binary strings', () => {
        const binaryStr = '1100101011110000';
        // @ts-ignore
        const result = binaryStringToUint8Array(binaryStr);
        expect(result).toEqual(new Uint8Array([202, 240]));
    });

    test('should convert a binary string with fewer than 8 bits', () => {
        const binaryStr = '110';
        // @ts-ignore
        const result = binaryStringToUint8Array(binaryStr);
        expect(result).toEqual(new Uint8Array([6]));
    });

    test('should convert a binary string with non-multiples of 8 bits', () => {
        const binaryStr = '110010101';
        // @ts-ignore
        const result = binaryStringToUint8Array(binaryStr);
        expect(result).toEqual(new Uint8Array([202, 1]));
    });

    test('should handle an empty binary string', () => {
        const binaryStr = '';
        // @ts-ignore
        const result = binaryStringToUint8Array(binaryStr);
        expect(result).toEqual(new Uint8Array([]));
    });
});
/**
 * Stores a second-level string in a set of 8-bit conversion integers in a Unit8Array and returns
 *
 * @param {string} binaryStr - The binary string to be converted.
 * @returns {Uint8Array} - The resulting Uint8Array containing the binary data.
 */
function binaryStringToUint8Array(binaryStr: string): Uint8Array {
    // Calculate the number of bytes needed to represent the binary string
    const byteCount = Math.ceil(binaryStr.length / 8);
    const byteArray = new Uint8Array(byteCount);

    // Convert each 8-character segment of the binary string into a byte and store in byteArray
    for (let i = 0; i < byteCount; i++) {
        const byteSegment = binaryStr.substr(i * 8, 8);  // Extract 8 characters
        byteArray[i] = parseInt(byteSegment, 2);  // Convert binary segment to byte
    }

    return byteArray;
}
