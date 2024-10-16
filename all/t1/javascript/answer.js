function numericalStrConvert(value) {
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