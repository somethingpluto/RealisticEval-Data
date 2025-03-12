/**
 * Sums up calibration values extracted from the document.
 * Each calibration value is formed by combining the first and last digits of numbers found in each line
 * into a two-digit number.
 *
 * @param {Iterable<string>} calibrationDocument - An iterable of strings, each representing a line of text.
 * @returns {number} The total sum of all calibration values.
 */
function sumCalibrationValues(calibrationDocument) {
    let totalSum = 0;

    for (const line of calibrationDocument) {
        // Extract all digits from the line
        const digits = line.match(/\d/g);

        if (digits && digits.length >= 2) {
            // Combine the first and last digits to form a two-digit number
            const calibrationValue = parseInt(digits[0] + digits[digits.length - 1]);
            totalSum += calibrationValue;
        }
    }

    return totalSum;
}
describe('TestSumCalibrationValues', () => {
    it('test_basic_calculations', () => {
        // Test with a simple input where lines contain at least two digits
        const document = [
            "Reading 1234 calibration",
            "Measure 5678 complete",
            "End of data 91011"
        ];
        expect(sumCalibrationValues(document)).toBe(163);
    });

    it('test_no_digits', () => {
        // Test lines with no digits
        const document = [
            "No numbers here",
            "Still no numbers"
        ];
        expect(sumCalibrationValues(document)).toBe(0);
    });

    it('test_empty_lines', () => {
        // Test with empty lines or lines with spaces
        const document = [
            "",
            "   "
        ];
        expect(sumCalibrationValues(document)).toBe(0);
    });

    it('test_mixed_content', () => {
        // Test with a mixture of valid and invalid lines
        const document = [
            "Good line 1524 end",
            "Bad line",
            "Another good line 7681"
        ];
        expect(sumCalibrationValues(document)).toBe(85);
    });
});
