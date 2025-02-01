/**
 * Converts the string representation of a score to its decimal value.
 * For example:
 *   input: "10/4"
 *   output: 2.5
 *
 * @param {string} scoreStr - The score as a string, can be a decimal or a fraction
 * @returns {number | null} - The decimal value of the score as a float, or null if the input is invalid
 */
function convertScoreToDecimal(scoreStr) {
    // Check if the input is a decimal number
    if (!isNaN(scoreStr)) {
        return parseFloat(scoreStr);
    }

    // Check if the input is a fraction
    const fractionParts = scoreStr.split('/');
    if (fractionParts.length === 2 && !isNaN(fractionParts[0]) && !isNaN(fractionParts[1])) {
        const numerator = parseFloat(fractionParts[0]);
        const denominator = parseFloat(fractionParts[1]);
        if (denominator !== 0) {
            return numerator / denominator;
        }
    }

    // If the input is neither a decimal nor a valid fraction, return null
    return null;
}
describe('TestConvertScoreToDecimal', () => {
    test('test_decimal_score', () => {
        // Test a simple decimal score
        expect(convertScoreToDecimal("2.5")).toBe(2.5);
    });

    test('test_fraction_score', () => {
        // Test a fraction score
        expect(convertScoreToDecimal("10/4")).toBe(2.5);
    });

    test('test_integer_score', () => {
        // Test an integer score represented as a string
        expect(convertScoreToDecimal("5")).toBe(5.0);
    });

    test('test_integer_divide_score', () => {
        // Test an integer divide score
        expect(convertScoreToDecimal("12/3")).toBe(4.0);
    });
});
