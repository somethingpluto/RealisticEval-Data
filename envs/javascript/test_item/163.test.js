/**
 * Stores a second-level string in a set of 8-bit conversion integers in a Uint8Array and returns
 *
 * @param {string} binaryStr - The binary string to be converted.
 * @returns {Uint8Array} - The resulting Uint8Array containing the binary question.
 */
// @ts-ignore
function binaryStringToUint8Array(binaryStr) {
    const uint8Array = new Uint8Array(Math.ceil(binaryStr.length / 8));
    for (let i = 0; i < uint8Array.length; i++) {
        let byte = 0;
        for (let j = 0; j < 8; j++) {
            if (i * 8 + j < binaryStr.length) {
                byte = (byte << 1) | (binaryStr[i * 8 + j] === '1' ? 1 : 0);
            }
        }
        uint8Array[i] = byte;
    }
    return uint8Array;
}
describe('binaryStringToUint8Array', () => {
    test('should convert a full byte binary string', () => {
        const binaryStr = '11001010';
        const result = binaryStringToUint8Array(binaryStr);
        expect(result).toEqual(new Uint8Array([202]));
    });

    test('should convert multiple full byte binary strings', () => {
        const binaryStr = '1100101011110000';
        const result = binaryStringToUint8Array(binaryStr);
        expect(result).toEqual(new Uint8Array([202, 240]));
    });

    test('should handle an empty binary string', () => {
        const binaryStr = '';
        const result = binaryStringToUint8Array(binaryStr);
        expect(result).toEqual(new Uint8Array([]));
    });

    test('should correctly convert binary string with leading zeros', () => {
        const binaryStr = '00101101';
        const result = binaryStringToUint8Array(binaryStr);
        expect(result).toEqual(new Uint8Array([45]));
    });

    test('should handle binary string with end padding of zeros', () => {
        const binaryStr = '11001010000'; // should be treated as '11001010 00000000'
        const result = binaryStringToUint8Array(binaryStr);
        expect(result).toEqual(new Uint8Array([202, 0]));
    });
});
