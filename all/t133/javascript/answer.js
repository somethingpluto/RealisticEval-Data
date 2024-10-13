function isSignificantNumber(input) {
    // Check if input is a string
    if (typeof input !== 'string') {
        return false;
    }

    // Trim whitespace from the input
    input = input.trim();

    // Check the length
    const length = input.length;
    if (length < 5 || length > 18) {
        return false;
    }

    // Check for significant number: all characters must be digits
    // and cannot start with '0' if the length is greater than 1
    if (!/^\d+$/.test(input) || (input.length > 1 && input[0] === '0')) {
        return false;
    }

    return true;
}
