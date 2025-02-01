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
    // Convert the float to a 64-bit integer representation
    const buffer = new ArrayBuffer(8);
    const view = new DataView(buffer);
    view.setFloat64(0, value);

    // Extract the 64-bit integer representation
    const int64 = view.getUint64(0, false);

    // Convert the integer to a hexadecimal string
    const hex = int64.toString(16);

    // Return the hexadecimal string
    return hex;
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
