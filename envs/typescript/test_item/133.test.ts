// Start of the code context
import { isNumeric } from 'lodash';

/**
 * Checks if the input string is a significant number.
 * A significant number is defined as a string that:
 * - Is between 5 and 18 characters in length.
 * - Consists only of digits (0-9).
 * - Does not start with '0' if its length is greater than 1.
 *
 * @param {string} input - The input string to check.
 * @returns {boolean} - Returns true if the input is a significant number; otherwise, false.
 */
function isSignificantNumber(input: string): boolean {
    if (!isNumeric(input)) {
        return false;
    }
    const trimmedInput = input.trim();
    return trimmedInput.length >= 5 && trimmedInput.length <= 18 && !trimmedInput.startsWith('0');
}
// End of the code context
describe('isSignificantNumber', () => {
    test('should return true for a valid significant number with exactly 5 digits', () => {
        expect(isSignificantNumber("12345")).toBe(true);
    });

    test('should return false for a number with leading zero', () => {
        expect(isSignificantNumber("01234")).toBe(false);
    });

    test('should return true for a valid significant number with exactly 18 digits', () => {
        expect(isSignificantNumber("123456789012345678")).toBe(true);
    });

    test('should return false for a number with less than 5 digits', () => {
        expect(isSignificantNumber("123")).toBe(false);
    });

    test('should return false for a number with more than 18 digits', () => {
        expect(isSignificantNumber("1234567890123456789")).toBe(false);
    });

    test('should return false for a number containing non-digit characters', () => {
        expect(isSignificantNumber("1234a")).toBe(false);
    });

    test('should return false for a single zero', () => {
        expect(isSignificantNumber("0")).toBe(false);
    });

    test('should return false for non-string input', () => {
        expect(isSignificantNumber(12345 as any)).toBe(false);
    });
});
