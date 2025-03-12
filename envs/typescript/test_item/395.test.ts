// Start of the code context
import { isNumeric } from 'lodash';

function sumCalibrationValues(calibrationDocument: Iterable<string>): number {
    let sum = 0;
    for (const line of calibrationDocument) {
        const numbers = line.match(/\d+/g);
        if (!numbers) continue;
        for (const numStr of numbers) {
            if (numStr.length >= 2) {
                const firstDigit = numStr[0];
                const lastDigit = numStr[numStr.length - 1];
                if (isNumeric(firstDigit) && isNumeric(lastDigit)) {
                    sum += parseInt(firstDigit + lastDigit, 10);
                }
            }
        }
    }
    return sum;
}
// End of the code context
describe('TestSumCalibrationValues', () => {
    describe('test_basic_calculations', () => {
        it('should correctly calculate the sum with basic input', () => {
            const document = [
                "Reading 1234 calibration",
                "Measure 5678 complete",
                "End of data 91011"
            ];
            expect(sumCalibrationValues(document)).toBe(163);
        });
    });

    describe('test_no_digits', () => {
        it('should return 0 when no digits are present', () => {
            const document = [
                "No numbers here",
                "Still no numbers"
            ];
            expect(sumCalibrationValues(document)).toBe(0);
        });
    });

    describe('test_empty_lines', () => {
        it('should return 0 for empty or whitespace-only lines', () => {
            const document = [
                "",
                "   "
            ];
            expect(sumCalibrationValues(document)).toBe(0);
        });
    });

    describe('test_mixed_content', () => {
        it('should correctly calculate the sum with mixed content', () => {
            const document = [
                "Good line 1524 end",
                "Bad line",
                "Another good line 7681"
            ];
            expect(sumCalibrationValues(document)).toBe(85);
        });
    });
});
