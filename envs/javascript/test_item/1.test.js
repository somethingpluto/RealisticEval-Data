/**
 * Converts the input string. First, checks if it is an integer. If it is, converts it to an integer.
 * If not, checks if it is a floating-point number. If it is, converts it to a floating-point number.
 * If it is neither, returns the original string.
 * 
 * @param {string} value - The input value as a string.
 * @returns {(number|string)} - The converted value or the original string.
 */
function numericalStrConvert(value) {
    // Check if the value is an integer
    if (/^-?\d+$/.test(value)) {
        return parseInt(value, 10);
    }
    
    // Check if the value is a floating-point number
    if (/^-?\d+(\.\d+)?$/.test(value)) {
        return parseFloat(value);
    }
    
    // If neither, return the original string
    return value;
}
describe('TestSmartConvert', () => {
    it('should convert to integer', () => {
        expect(numericalStrConvert("123")).toBe(123);
    });

    it('should convert to float', () => {
        expect(numericalStrConvert("123.45")).toBe(123.45);
    });

    it('should remain a string for non-numeric input', () => {
        expect(numericalStrConvert("abc")).toBe("abc");
    });

    it('should convert to negative integer', () => {
        expect(numericalStrConvert("-456")).toBe(-456);
    });

    it('should convert to negative float', () => {
        expect(numericalStrConvert("-456.78")).toBe(-456.78);
    });
});
