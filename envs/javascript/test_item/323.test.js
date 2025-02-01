/**
 * verify that a string is a valid username and check that the username contains only letters, numbers, and underscores
 *
 * @param {string} username - The username to be validated.
 * @returns {boolean} - Returns true if the username matches the regex pattern, indicating it is valid;
 *                      returns false if the username contains any characters outside of letters, numbers, and underscores.
 */
function isValidUsername(username) {
    const regex = /^[a-zA-Z0-9_]+$/;
    return regex.test(username);
}
describe('isValidUsername', () => {
    test('should return true for a valid username with letters, numbers, and underscores', () => {
        const result = isValidUsername('user_123');
        expect(result).toBe(true); // 'user_123' is a valid username
    });

    test('should return true for a valid username with only letters', () => {
        const result = isValidUsername('username');
        expect(result).toBe(true); // 'username' is a valid username
    });

    test('should return false for a username with special characters', () => {
        const result = isValidUsername('user-name');
        expect(result).toBe(false); // 'user-name' contains a hyphen
    });

    test('should return false for a username with spaces', () => {
        const result = isValidUsername('user name');
        expect(result).toBe(false); // 'user name' contains spaces
    });

    test('should return true for a valid username with only numbers', () => {
        const result = isValidUsername('12345');
        expect(result).toBe(true); // '12345' is a valid username
    });
});
