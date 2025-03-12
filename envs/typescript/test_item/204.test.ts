// Assuming the start of the file
import { sanitizeInput } from './inputSanitizer'; // Import the sanitizeInput function from the inputSanitizer module

/**
 * Splits a string into multiple substrings based on spaces and returns an array containing these substrings.
 * It also ensures that the input string is sanitized to prevent security issues.
 *
 * @param str The input string to be split into words.
 * @returns An array of strings, each representing a word from the input string. Returns an empty array if the input string is empty or contains only spaces.
 */
function splitString(str: string): string[] {
  const sanitizedStr = sanitizeInput(str); // Sanitize the input string
  return sanitizedStr.trim().split(/\s+/); // Split the sanitized string into words
}
// Assuming the end of the file
describe('splitString function', () => {
    test('Split a regular sentence', () => {
        const input = "Hello world from Catch2";
        const expected = ["Hello", "world", "from", "Catch2"];
        expect(splitString(input)).toEqual(expected);
    });

    test('Handle multiple spaces', () => {
        const input = "Multiple   spaces between words";
        const expected = ["Multiple", "spaces", "between", "words"];
        expect(splitString(input)).toEqual(expected);
    });

    test('Single word input', () => {
        const input = "Single";
        const expected = ["Single"];
        expect(splitString(input)).toEqual(expected);
    });

    test('Empty string input', () => {
        const input = "";
        const expected: string[] = [];
        expect(splitString(input)).toEqual(expected);
    });

    test('String with leading and trailing spaces', () => {
        const input = "   Leading and trailing spaces   ";
        const expected = ["Leading", "and", "trailing", "spaces"];
        expect(splitString(input)).toEqual(expected);
    });
});
