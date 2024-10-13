function numericalStrConvert(value) {
    /**
     * Convert the input string. First, check if it is an integer. If it is, convert it to an integer.
     * If not, check if it is a floating-point number. If it is, convert it to a floating-point number.
     * If it is neither, return the original string.
     * 
     * @param {string} value - The input value as a string.
     * @returns {number|string} - The converted value or the original string.
     */
    
    // Attempt to parse the string as an integer
    const intValue = parseInt(value);
    if (!isNaN(intValue) && intValue.toString() === value) {
        return intValue;
    }

    // If not an integer, attempt to parse the string as a floating-point number
    const floatValue = parseFloat(value);
    if (!isNaN(floatValue) && floatValue.toString() === value) {
        return floatValue;
    }

    // If not an integer or a floating-point number, return the original string
    return value;
}