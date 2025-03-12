/**
 * Converts a floating-point number to its hexadecimal representation.
 *
 * @param {number} value The float value to be converted to hexadecimal.
 * @return {string} A string containing the hexadecimal representation of the
 *         input float.
 *
 * @note The output string will be in lowercase hexadecimal format.
 */
function floatToHex(value) {
    // Convert the float to a 32-bit integer representation
    const buffer = new ArrayBuffer(4);
    const floatView = new Float32Array(buffer);
    const intView = new Uint32Array(buffer);
    
    floatView[0] = value;
    const intValue = intView[0];
    
    // Convert the integer to a hexadecimal string
    const hexString = intValue.toString(16);
    
    // Ensure the hexadecimal string is 8 characters long
    return hexString.padStart(8, '0');
}
describe("floatToHex tests", () => {
    test("Test with positive float 123.456", () => {
        const input = 123.456;
        const expected = "42f6e979";
        expect(floatToHex(input)).toBe(expected);
    });

    test("Test with negative float -123.456", () => {
        const input = -123.456;
        const expected = "c2f6e979";
        expect(floatToHex(input)).toBe(expected);
    });

    test("Test with zero", () => {
        const input = 0.0;
        const expected = "00000000";
        expect(floatToHex(input)).toBe(expected);
    });

    test("Test with small positive float 0.0001", () => {
        const input = 0.0001;
        const expected = "38d1b717";
        expect(floatToHex(input)).toBe(expected);
    });

    test("Test with large float 1e30", () => {
        const input = 1e30;
        const expected = "7149f2ca";
        expect(floatToHex(input)).toBe(expected);
    });
});
