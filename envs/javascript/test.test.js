/**
 * Convert the input string, first see if it is an integer,
 * if it is converted to an integer, if it is not, see if it is a floating point number,
 * if yes, convert to a floating point number, if neither, return the original string
 *
 * @param {string} value - The input value string
 * @returns {number|string} - Converted result
 */
function numericalStrConvert(value) {
    // Try to convert to integer
    const intVal = parseInt(value, 10);
    if (!isNaN(intVal) && intVal.toString() === value) {
        return intVal;
    }

    // Try to convert to float
    const floatVal = parseFloat(value);
    if (!isNaN(floatVal) && floatVal.toString() === value) {
        return floatVal;
    }

    // Return original string if not a number
    return value;
}
describe('numericalStrConvert', () => {
    test('should convert to integer', () => {
        expect(numericalStrConvert("123")).toBe(123);
    });

    test('should convert to float', () => {
        expect(numericalStrConvert("123.45")).toBe(123.45);
    });

    test('should remain a string for non-numeric input', () => {
        expect(numericalStrConvert("abc")).toBe("abc");
    });

    test('should convert to negative integer', () => {
        expect(numericalStrConvert("-456")).toBe(-456);
    });

    test('should convert to negative float', () => {
        expect(numericalStrConvert("-456.78")).toBe(-456.78);
    });
});
