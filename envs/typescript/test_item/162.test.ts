import { sanitizeInput } from './inputSanitizer'; // Assuming the existence of an input sanitizer module

/**
 * Converts the array of Boolean values to a binary string representation.
 * The function now includes input validation and sanitization.
 *
 * @param {boolean[]} boolArray - An array of boolean values.
 * @returns {string} A binary string where '1' represents true and '0' represents false.
 * @throws Will throw an error if the input is not an array of booleans.
 */
function boolArrayToBinaryString(boolArray: boolean[]): string {
  // Validate and sanitize the input
  const sanitizedArray = sanitizeInput(boolArray);

  // Convert the sanitized array to a binary string
  return sanitizedArray.map(value => value ? '1' : '0').join('');
}
describe('boolArrayToBinaryString', () => {
    test('converts an array of all true values', () => {
        const boolArray = [true, true, true];
        const expected = '111';
        // @ts-ignore
        expect(boolArrayToBinaryString(boolArray)).toBe(expected);
    });

    test('converts an array of all false values', () => {
        const boolArray = [false, false, false];
        const expected = '000';
        // @ts-ignore
        expect(boolArrayToBinaryString(boolArray)).toBe(expected);
    });

    test('converts an array with a mix of true and false values', () => {
        const boolArray = [true, false, true, false];
        const expected = '1010';
        // @ts-ignore
        expect(boolArrayToBinaryString(boolArray)).toBe(expected);
    });

    test('handles an empty array', () => {
        const boolArray: boolean[] = [];
        const expected = '';
        // @ts-ignore
        expect(boolArrayToBinaryString(boolArray)).toBe(expected);
    });

    test('handles a single boolean value', () => {
        const boolArray = [true];
        const expected = '1';
        // @ts-ignore
        expect(boolArrayToBinaryString(boolArray)).toBe(expected);
    });
});
