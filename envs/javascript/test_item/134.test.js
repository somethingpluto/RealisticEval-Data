/**
 * Checks whether the provided username is valid.
 * A valid username is defined as a string that:
 * - Has a length between 5 and 16 characters (inclusive).
 * - Contains only alphanumeric characters (letters and digits) and spaces.
 *
 * @param {string} username - The username to validate.
 * @returns {boolean} - Returns true if the username is valid; otherwise, false.
 */
function isValidUsername(username) {
    // Check if the username is a string
    if (typeof username !== 'string') {
        return false;
    }

    // Check if the username length is between 5 and 16 characters
    if (username.length < 5 || username.length > 16) {
        return false;
    }

    // Check if the username contains only alphanumeric characters and spaces
    const regex = /^[a-zA-Z0-9 ]+$/;
    return regex.test(username);
}
describe('isValidUsername', () => {
    test('valid username with alphanumeric characters', () => {
        expect(isValidUsername('User123')).toBe(true);
    });

    test('valid username with spaces', () => {
        expect(isValidUsername('User 123')).toBe(true);
    });

    test('invalid username that is too short', () => {
        expect(isValidUsername('User')).toBe(false);
    });

    test('invalid username that is too long', () => {
        expect(isValidUsername('ThisIsAVeryLongUsername')).toBe(false);
    });

    test('invalid username with special characters', () => {
        expect(isValidUsername('User!')).toBe(false);
    });

    test('invalid username with only spaces', () => {
        expect(isValidUsername('     ')).toBe(false);
    });

    test('invalid input type (number)', () => {
        expect(isValidUsername(12345)).toBe(false);
    });
});
