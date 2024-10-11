describe('sum_calibration_values', () => {
    test('should sum up calibration values correctly', () => {
        const calibrationDocument = [
            "1abc2",
            "pqr3stu4",
            "abcd56efgh78"
        ];
        expect(sum_calibration_values(calibrationDocument)).toBe(12 + 34 + 57);
    });

    test('should handle lines with no numbers', () => {
        const calibrationDocument = [
            "no numbers here",
            "another line without numbers"
        ];
        expect(sum_calibration_values(calibrationDocument)).toBe(0);
    });

    test('should handle lines with multiple numbers', () => {
        const calibrationDocument = [
            "123abc456",
            "789def012"
        ];
        expect(sum_calibration_values(calibrationDocument)).toBe(16 + 72);
    });

    test('should handle empty lines', () => {
        const calibrationDocument = [
            "",
            ""
        ];
        expect(sum_calibration_values(calibrationDocument)).toBe(0);
    });
});