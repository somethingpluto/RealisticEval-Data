describe('sumCalibrationValues', () => {
    it('should sum up calibration values correctly', () => {
        const calibrationDocument = [
            '1abc2',
            'pqr3stu4',
            '5v6w7x8y9z'
        ];
        const result = sumCalibrationValues(calibrationDocument);
        expect(result).toBe(12 + 34 + 59); // 12 (from "1abc2") + 34 (from "pqr3stu4") + 59 (from "5v6w7x8y9z")
    });

    it('should handle empty lines gracefully', () => {
        const calibrationDocument = [
            '',
            'no numbers here',
            '123456'
        ];
        const result = sumCalibrationValues(calibrationDocument);
        expect(result).toBe(16); // 16 (from "123456")
    });

    it('should handle lines with no numbers', () => {
        const calibrationDocument = [
            'abcdef',
            'ghijkl'
        ];
        const result = sumCalibrationValues(calibrationDocument);
        expect(result).toBe(0); // No numbers, so sum should be 0
    });
});