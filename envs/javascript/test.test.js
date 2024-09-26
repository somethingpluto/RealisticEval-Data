/**
 * Convert the input string. First check if it's an integer, if so, convert to an integer.
 * If not, check if it's a floating-point number, if yes, convert to a floating-point number;
 * if neither, return the original string.
 * @param {string} value - Input value as a string
 * @returns {number|string} - Converted result
 */
function numericalStrConvert(value) {
    // Attempt to convert to integer
    const intValue = parseInt(value, 10);
    if (!isNaN(intValue) && intValue.toString() === value) {
        return intValue;  // Return as integer if it matches original string
    }

    // If not an integer, attempt to convert to float
    const floatValue = parseFloat(value);
    if (!isNaN(floatValue) && floatValue.toString() === value) {
        return floatValue;  // Return as float if it matches original string
    }

    // If neither, return the original string
    return value;
}
describe('TestSmartConvert', () => {
    test('should convert integer', () => {
        expect(numericalStrConvert("123")).toBe(123);
    });

    test('should convert float', () => {
        expect(numericalStrConvert("123.45")).toBe(123.45);
    });

    test('should remain a string for non-numeric input', () => {
        expect(numericalStrConvert("abc")).toBe("abc");
    });

    test('should convert negative integer', () => {
        expect(numericalStrConvert("-456")).toBe(-456);
    });

    test('should convert negative float', () => {
        expect(numericalStrConvert("-456.78")).toBe(-456.78);
    });
});
