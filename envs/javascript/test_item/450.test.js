/**
 * Checks whether the provided password meets the specified format requirements:
 * - At least one number
 * - At least one lowercase letter
 * - At least one uppercase letter
 * - At least one punctuation mark
 * - Minimum length of 8 characters
 *
 * @param {string} password - The password string to validate
 * @returns {boolean} Returns true if the password meets all requirements; otherwise, false.
 */
function isValidPassword(password) {
    // Check if the password length is at least 8 characters
    if (password.length < 8) {
        return false;
    }

    // Regular expressions to check for required characters
    const hasNumber = /\d/.test(password);
    const hasLowercase = /[a-z]/.test(password);
    const hasUppercase = /[A-Z]/.test(password);
    const hasPunctuation = /[!@#$%^&*(),.?":{}|<>]/.test(password);

    // Return true only if all conditions are met
    return hasNumber && hasLowercase && hasUppercase && hasPunctuation;
}
describe('Password Validator Tests', () => {
    test('Valid password', () => {
        expect(isValidPassword("Password1!")).toBe(true);
    });

    test('Password without a number', () => {
        expect(isValidPassword("Password!")).toBe(false);
    });

    test('Password without an uppercase letter', () => {
        expect(isValidPassword("password1!")).toBe(false);
    });

    test('Password without a lowercase letter', () => {
        expect(isValidPassword("PASSWORD1!")).toBe(false);
    });

    test('Password without a punctuation mark', () => {
        expect(isValidPassword("Password1")).toBe(false);
    });

    test('Password shorter than 8 characters', () => {
        expect(isValidPassword("Pass1!")).toBe(false);
    });
});
