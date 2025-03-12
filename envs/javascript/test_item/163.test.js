/**
 * Stores a second-level string in a set of 8-bit conversion integers in a Uint8Array and returns
 *
 * @param {string} binaryStr - The binary string to be converted.
 * @returns {Uint8Array} - The resulting Uint8Array containing the binary question.
 */
function binaryStringToUint8Array(binaryStr) {
    // Ensure the binary string length is a multiple of 8
    if (binaryStr.length % 8 !== 0) {
        throw new Error("The length of the binary string must be a multiple of 8.");
    }

    // Calculate the number of bytes needed
    const numBytes = binaryStr.length / 8;

    // Create a new Uint8Array with the calculated number of bytes
    const uint8Array = new Uint8Array(numBytes);

    // Loop through the binary string in chunks of 8 bits
    for (let i = 0; i < binaryStr.length; i += 8) {
        // Extract the 8-bit chunk
        const byteStr = binaryStr.substring(i, i + 8);

        // Convert the 8-bit binary string to an integer
        const byteValue = parseInt(byteStr, 2);

        // Store the integer in the Uint8Array
        uint8Array[i / 8] = byteValue;
    }

    // Return the resulting Uint8Array
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
