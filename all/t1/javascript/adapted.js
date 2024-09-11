function convertString(input) {
    // First try to convert the input to an integer
    const asInteger = parseInt(input);

    // Check if the parsed integer is a valid number and the input has no extraneous characters
    if (!isNaN(asInteger) && asInteger.toString() === input.trim()) {
        return asInteger;
    }

    // If not an integer, try to convert the input to a float
    const asFloat = parseFloat(input);

    // Check if the parsed float is a valid number and the input has no extraneous characters
    if (!isNaN(asFloat) && asFloat.toString() === input.trim()) {
        return asFloat;
    }

    // If neither, return the original input
    return input;
}