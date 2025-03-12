/**
 * Count the number of numbers in a string
 *
 * @param {string} str - The string from which to count numeric digits.
 * @returns {number} - The total count of numeric digits found in the string.
 */
function countNumbers(str) {
    let count = 0;
    for (let i = 0; i < str.length; i++) {
        if (!isNaN(str[i]) && str[i] !== ' ') {
            count++;
        }
    }
    return count;
}
// Jest test cases for countNumbers function
describe('countNumbers', () => {
    test('should return the correct count for a string with multiple numbers', () => {
        const result = countNumbers('There are 123 numbers in this string.');
        expect(result).toBe(3); // '123' contains three numeric characters
    });

    test('should return 0 for a string with no numbers', () => {
        const result = countNumbers('No numbers here!');
        expect(result).toBe(0); // No numeric characters in 'No numbers here!'
    });

    test('should return the correct count for a string with mixed characters', () => {
        const result = countNumbers('Room 101 and Room 102');
        expect(result).toBe(6); // '101' and '102' together contain six numeric characters
    });

    test('should return the correct count for a string with only numbers', () => {
        const result = countNumbers('1234567890');
        expect(result).toBe(10); // '1234567890' contains ten numeric characters
    });

    test('should return 0 for an empty string', () => {
        const result = countNumbers('');
        expect(result).toBe(0); // An empty string contains no numeric characters
    });
});
