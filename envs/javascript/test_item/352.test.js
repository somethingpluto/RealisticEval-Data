/**
 * Converts a hexadecimal string into a byte array. Hexadecimal strings are often used to represent binary data
 * in a readable format, especially in networking, cryptography, and systems programming.
 *
 * @param {string} hexStr - The hexadecimal string to be converted. This string should only contain hexadecimal characters
 *                          (0-9, A-F, a-f). If the string has an odd number of characters, a leading zero is added to ensure
 *                          proper conversion.
 * @returns {Uint8Array} A byte array representing the binary data encoded in the hex string.
 */
function hexStringToByteArray(hexStr) {
    // Ensure the hex string has an even length
    if (hexStr.length % 2 !== 0) {
        hexStr = '0' + hexStr;
    }

    // Create an empty array to hold the byte array
    const byteArray = new Uint8Array(hexStr.length / 2);

    // Convert the hex string to a byte array
    for (let i = 0; i < hexStr.length; i += 2) {
        byteArray[i / 2] = parseInt(hexStr.substr(i, 2), 16);
    }

    return byteArray;
}
describe('hexStringToByteArray', () => {
    test('normal hex string', () => {
        const hexStr = "1a3f";
        const expected = new Uint8Array([0x1A, 0x3F]);
        expect(hexStringToByteArray(hexStr)).toEqual(expected);
        // Assertion message is not included in Jest by default
    });

    test('odd length hex string', () => {
        const hexStr = "123";
        const expected = new Uint8Array([0x01, 0x23]);
        expect(hexStringToByteArray(hexStr)).toEqual(expected);
    });

    test('empty string', () => {
        const hexStr = "";
        const expected = new Uint8Array([]);
        expect(hexStringToByteArray(hexStr)).toEqual(expected);
    });

    test('hex string with uppercase', () => {
        const hexStr = "1A3F";
        const expected = new Uint8Array([0x1A, 0x3F]);
        expect(hexStringToByteArray(hexStr)).toEqual(expected);
    });
});
