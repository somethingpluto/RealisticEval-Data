/**
 * Parses a given hexadecimal string into its corresponding floating-point number and returns the float value.
 * @param {string} hexStr - The hexadecimal string to parse.
 * @return {number} The parsed floating-point number.
 */
function hexStringToFloat(hexStr) {
    const intBits = parseInt(hexStr, 16);
    const sign = (intBits >> 31) ? -1 : 1;
    const exponent = ((intBits >> 23) & 0xFF) - 127;
    const mantissa = (intBits & 0x7FFFFF) | 0x800000;
    const floatVal = sign * mantissa * Math.pow(2, exponent - 23);
    return floatVal;
}
describe("Hexadecimal String to Float Conversion", () => {
    
    test("Positive number: 40490FDB", () => {
        const hexStr = "40490FDB"; // 3.14159 in float
        const result = hexStringToFloat(hexStr);
        expect(result).toBeCloseTo(3.14159, 5); // Use toBeCloseTo for floating-point comparison
    });

    test("Negative number: C0490FDB", () => {
        const hexStr = "C0490FDB"; // -3.14159 in float
        const result = hexStringToFloat(hexStr);
        expect(result).toBeCloseTo(-3.14159, 5);
    });

    test("Zero: 00000000", () => {
        const hexStr = "00000000"; // 0.0 in float
        const result = hexStringToFloat(hexStr);
        expect(result).toBeCloseTo(0.0, 5);
    });

    test("Small positive number: 3F800000", () => {
        const hexStr = "3F800000"; // 1.0 in float
        const result = hexStringToFloat(hexStr);
        expect(result).toBeCloseTo(1.0, 5);
    });

    test("Small negative number: BF800000", () => {
        const hexStr = "BF800000"; // -1.0 in float
        const result = hexStringToFloat(hexStr);
        expect(result).toBeCloseTo(-1.0, 5);
    });
});
