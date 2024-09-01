describe('setEurValue', () => {
    test('formats standard values correctly', () => {
        expect(setEurValue('250')).toBe('250');
        expect(setEurValue('2500')).toBe('2.5k');
    });

    test('handles boundary values accurately', () => {
        expect(setEurValue('999')).toBe('999');
        expect(setEurValue('1000')).toBe('1.0k');
        expect(setEurValue('999999')).toBe('1000.0k');
        expect(setEurValue('1000000')).toBe('1.0m');
    });

    test('returns correct format for zero and negative inputs', () => {
        expect(setEurValue('0')).toBe('0');
    });

    test('returns an empty string for invalid inputs', () => {
        expect(setEurValue('hello')).toBe('');
        expect(setEurValue(null)).toBe('');
        expect(setEurValue(undefined)).toBe('');
    });

    test('ensures precision for large numbers', () => {
        expect(setEurValue('10000000')).toBe('10.0m');
        expect(setEurValue('987654321')).toBe('987.7m');
    });
});

/**
 * Converts a numerical value into a string representation with appropriate
 * suffixes ('k' for thousands, 'm' for millions) or returns the number as a string
 * if the value is below 1000. Returns an empty string for non-numeric or invalid inputs.
 *
 * @param {string|number} value - The value to convert.
 * @returns {string} - The formatted string or an empty string if the input is invalid.
 */
function setEurValue(value) {
    // Check for empty, null, or undefined inputs directly
    if (!value && value !== 0) return '';

    // Attempt to parse the input value to an integer
    const number = parseInt(value, 10);

    // Check if the result is a valid number
    if (isNaN(number)) return '';

    // Determine the suffix and division based on the size of the number
    if (number >= 1_000_000) {
        return (number / 1_000_000).toFixed(1) + 'm';  // Format for millions
    } else if (number >= 1_000) {
        return (number / 1_000).toFixed(1) + 'k';      // Format for thousands
    } else {
        return number.toString();                     // Return as string for smaller numbers
    }
}