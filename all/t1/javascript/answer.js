function numericalStrConvert(value) {


    // Check if the value is an integer
    const intValue = parseInt(value, 10);
    if (!isNaN(intValue) && intValue.toString() === value) {
        return intValue;
    }

    // Check if the value is a float
    const floatValue = parseFloat(value);
    if (!isNaN(floatValue) && floatValue.toString() === value) {
        return floatValue;
    }

    // Return the original string if neither
    return value;
}