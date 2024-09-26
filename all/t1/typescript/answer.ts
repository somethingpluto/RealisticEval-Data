/**
 * Convert the input string. First check if it's an integer, if so, convert to an integer.
 * If not, check if it's a floating-point number, if yes, convert to a floating-point number;
 * if neither, return the original string.
 * @param value - Input value as a string
 * @returns number | string - Converted result
 */
function numericalStrConvert(value: string): number | string {
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