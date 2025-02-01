/**
 * Extracts a numeric value from the input string based on the given regex pattern.
 *
 * @param {any} x - The input from which to extract the value. It will be converted to a string.
 * @param {string} pattern - The regular expression pattern to use for matching.
 * @returns {number|string} - The extracted weight value if a match is found, otherwise an empty string.
 */
function cleanPattern(x, pattern) {
    const str = String(x);
    const match = str.match(pattern);
    return match ? Number(match[0]) : '';
}
describe('TestCleanPattern', () => {
    let pattern;

    beforeEach(() => {
        // Sets up a common regex pattern for testing
        pattern = /(\d+\.?\d*) kg/;
    });

    it('test_valid_integer_weight', () => {
        // Test case for valid integer weight
        const inputString = "The weight is 25 kg";
        const result = cleanPattern(inputString, pattern);
        expect(result).toBe(25.0);
    });

    it('test_valid_float_weight', () => {
        // Test case for valid float weight
        const inputString = "Weight measured at 15.75 kg";
        const result = cleanPattern(inputString, pattern);
        expect(result).toBe(15.75);
    });

    it('test_no_weight_found', () => {
        // Test case where no weight is present
        const inputString = "No weight provided.";
        const result = cleanPattern(inputString, pattern);
        expect(result).toBe('');
    });

    it('test_invalid_float_conversion', () => {
        // Test case for non-numeric weight
        const inputString = "The weight is thirty kg";
        const result = cleanPattern(inputString, pattern);
        expect(result).toBe('');
    });

    it('test_weight_with_extra_text', () => {
        // Test case for weight with additional text
        const inputString = "The total weight is 45.3 kg as per the last measurement.";
        const result = cleanPattern(inputString, pattern);
        expect(result).toBe(45.3);
    });
});
