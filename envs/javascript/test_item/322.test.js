/**
 * Verify that a string is a valid email address
 *
 * @param {string} email - The email address to be validated.
 * @returns {boolean} - Returns true if the email matches the regex pattern, indicating it is valid,
 *                      or false otherwise.
 */
function isValidEmail(email) {
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
}
describe('isValidEmail', () => {
    test('should return true for a valid simple email', () => {
        const result = isValidEmail('test@example.com');
        expect(result).toBe(true); // 'test@example.com' is a valid email
    });

    test('should return true for a valid email with subdomain', () => {
        const result = isValidEmail('user@mail.example.com');
        expect(result).toBe(true); // 'user@mail.example.com' is a valid email
    });

    test('should return false for an email missing the @ symbol', () => {
        const result = isValidEmail('invalid-email.com');
        expect(result).toBe(false); // 'invalid-email.com' is missing the @ symbol
    });

    test('should return false for an email missing the domain part', () => {
        const result = isValidEmail('user@.com');
        expect(result).toBe(false); // 'user@.com' is missing a valid domain name
    });

    test('should return false for an email with spaces', () => {
        const result = isValidEmail('user name@example.com');
        expect(result).toBe(false); // 'user name@example.com' contains spaces
    });
});
