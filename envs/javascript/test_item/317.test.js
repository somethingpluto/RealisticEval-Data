/**
 * Count the number of letters in a string.
 *
 * @param {string} str - The input string from which to count letters.
 * @returns {number} - The count of letters in the string.
 */
function countLetters(str) {
    // Use a regular expression to match only letters (a-z, A-Z)
    const letterMatches = str.match(/[a-zA-Z]/g);
    
    // If there are no matches, return 0; otherwise, return the length of the matches array
    return letterMatches ? letterMatches.length : 0;
}
describe('countLetters', () => {
    test('should return 10 for the string "Hello, World!"', () => {
        expect(countLetters("Hello, World!")).toBe(10);
    });

    test('should return 0 for a string with no letters "12345"', () => {
        expect(countLetters("12345")).toBe(0);
    });

    test('should return 6 for the string "abc 123 xyz!"', () => {
        expect(countLetters("abc 123 xyz!")).toBe(6);
    });

    test('should return 0 for an empty string', () => {
        expect(countLetters("")).toBe(0);
    });

    test('should return 3 for the string "A1B2C3!@#"', () => {
        expect(countLetters("A1B2C3!@#")).toBe(3);
    });

    test('should return 5 for a string with mixed case "AbCdE"', () => {
        expect(countLetters("AbCdE")).toBe(5);
    });

    test('should return 8 for a string with special characters "Hello@2024!"', () => {
        expect(countLetters("Hello@2024!")).toBe(5);
    });
});
