function numericalStrConvert(value: string): number | string {
    const intValue = parseInt(value);
    if (!isNaN(intValue)) {
        return intValue;
    }

    const floatValue = parseFloat(value);
    if (!isNaN(floatValue)) {
        return floatValue;
    }

    return value;
}