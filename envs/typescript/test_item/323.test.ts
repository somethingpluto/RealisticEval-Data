import { sanitizeInput } from 'some-sanitization-library'; // Replace with actual library import

/**
 * Verifies that a string is a valid username and checks that the username contains only letters, numbers, and underscores.
 * It also ensures that the username is not empty and does not exceed 20 characters.
 *
 * @param {string} username - The username to be validated.
 * @returns {boolean} - Returns true if the username matches the regex pattern, is not empty, and does not exceed 20 characters;
 *                      returns false otherwise.
 */
function isValidUsername(username: string): boolean {
  const sanitizedUsername = sanitizeInput(username);
  const isValidLength = sanitizedUsername.length > 0 && sanitizedUsername.length <= 20;
  const isValidPattern = /^[a-zA-Z0-9_]+$/.test(sanitizedUsername);
  return isValidLength && isValidPattern;
}
describe('isValidUsername', () => {
    test('should return true for a valid username with letters, numbers, and underscores', () => {
        const result: boolean = isValidUsername('user_123');
        expect(result).toBe(true); // 'user_123' is a valid username
    });

    test('should return true for a valid username with only letters', () => {
        const result: boolean = isValidUsername('username');
        expect(result).toBe(true); // 'username' is a valid username
    });

    test('should return false for a username with special characters', () => {
        const result: boolean = isValidUsername('user-name');
        expect(result).toBe(false); // 'user-name' contains a hyphen
    });

    test('should return false for a username with spaces', () => {
        const result: boolean = isValidUsername('user name');
        expect(result).toBe(false); // 'user name' contains spaces
    });

    test('should return true for a valid username with only numbers', () => {
        const result: boolean = isValidUsername('12345');
        expect(result).toBe(true); // '12345' is a valid username
    });
});
