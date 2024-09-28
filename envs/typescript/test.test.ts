/**
 * Convert the input string. First, see if it is an integer. If it is, convert to an integer.
 * If it is not, see if it is a floating point number. If yes, convert to a floating point number.
 * If neither, return the original string.
 *
 * @param {string} value - The input value string
 * @returns {number|string} - Converted result
 */
function numericalStrConvert(value: string): number | string {
    const intValue = parseInt(value, 10);
    if (!isNaN(intValue) && intValue.toString() === value) {
        return intValue;
    }

    const floatValue = parseFloat(value);
    if (!isNaN(floatValue) && floatValue.toString() === value) {
        return floatValue;
    }

    return value;
}
describe('TestSmartConvert', () => {
    it('should convert to integer', () => {
        expect(numericalStrConvert("123")).toBe(123);
    });

    it('should convert to float', () => {
        expect(numericalStrConvert("123.45")).toBe(123.45);
    });

    it('should remain a string when converting non-numeric strings', () => {
        expect(numericalStrConvert("abc")).toBe("abc");
    });

    it('should convert to negative integer', () => {
        expect(numericalStrConvert("-456")).toBe(-456);
    });

    it('should convert to negative float', () => {
        expect(numericalStrConvert("-456.78")).toBe(-456.78);
    });
});

