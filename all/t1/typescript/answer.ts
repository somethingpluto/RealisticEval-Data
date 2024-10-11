/**
 * Convert the input string.
 * First, check if it's an integer. If so, convert to an integer.
 * If not, check if it's a floating point number. If yes, convert to a float.
 * If neither, return the original string.
 *
 * @param value - input value string
 * @returns number | string - converted value
 */
function numericalStrConvert(value: string): number | string {

    const intVal = parseInt(value, 10);
    if (!isNaN(intVal) && intVal.toString() === value) {
        return intVal;
    }

    const floatVal = parseFloat(value);
    if (!isNaN(floatVal) && floatVal.toString() === value) {
        return floatVal;
    }

    return value;
}