/**
 * Parses a given hexadecimal string into its corresponding floating-point number and returns the float value.
 * @param {string} hexStr - The hexadecimal string to parse.
 * @return {number} The parsed floating-point number.
 */
function hexStringToFloat(hexStr) {
    // Convert the hexadecimal string to a 32-bit integer
    const intValue = parseInt(hexStr, 16);
    
    // Create a new Float32Array and set the value using the 32-bit integer
    const floatArray = new Float32Array(1);
    floatArray[0] = intValue;
    
    // Return the floating-point number
    return floatArray[0];
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
