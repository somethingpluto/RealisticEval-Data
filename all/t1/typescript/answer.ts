function numericalStrConvert(value: string): number | string {
    // try converting to int
    const intValue = parseInt(value);
    if (!isNaN(intValue)) {
        return intValue;
    }

    // try converting to float
    const floatValue = parseFloat(value);
    if (!isNaN(floatValue)) {
        return floatValue;
    }

    // return original string if neither conversion was successful
    return value;
}