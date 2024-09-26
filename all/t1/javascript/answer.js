function numericalStrConvert(value) {
    /**
     * Convert the input string, first see if it is an integer, if it is converted to an integer,
     * if not, see if it is a floating point number, if yes, convert to a floating point number,
     * if neither, return the original string.
     *
     * @param {string} value - Input value as string.
     * @returns {number|string} - The converted result.
     */
    try {
        let intValue = parseInt(value);
        if (!isNaN(intValue) && intValue.toString() === value) {
            return intValue;
        }
    } catch (e) {
        // Not an integer, proceed to check for float.
    }

    try {
        let floatValue = parseFloat(value);
        if (!isNaN(floatValue) && floatValue.toString() === value) {
            return floatValue;
        }
    } catch (e) {
        // Not a float, return the original string.
    }

    return value;
}