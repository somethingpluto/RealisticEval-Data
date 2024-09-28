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