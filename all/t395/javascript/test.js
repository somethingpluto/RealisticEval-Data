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