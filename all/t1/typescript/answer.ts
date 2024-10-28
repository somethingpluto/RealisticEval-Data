function numericalStrConvert(value: string): number | string {
    const intValue = parseInt(value);
    if (!isNaN(intValue) && intValue.toString() === value) {
        return intValue;
    }
    const floatValue = parseFloat(value);
    if (!isNaN(floatValue) && floatValue.toString() === value) {
        return floatValue;
    }
    return value;
}
