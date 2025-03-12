/**
 * Check if the provided password is strong.
 *
 * A strong password must satisfy the following criteria:
 * - At least one lowercase letter
 * - At least one uppercase letter
 * - At least one number
 * - At least 8 characters long
 *
 * @param {string} password - The password to check.
 * @returns {boolean} - True if the password is strong, False otherwise.
 */
function isStrongPassword(password) {
    // Check if the password is at least 8 characters long
    if (password.length < 8) {
        return false;
    }

    // Regular expressions to check for at least one lowercase letter, one uppercase letter, and one number
    const hasLowercase = /[a-z]/.test(password);
    const hasUppercase = /[A-Z]/.test(password);
    const hasNumber = /\d/.test(password);

    // Return true only if all criteria are met
    return hasLowercase && hasUppercase && hasNumber;
}
describe('TestStrongPassword', () => {
    it('should validate a strong password that meets all criteria', () => {
        expect(isStrongPassword("StrongPass1")).toBe(true);
    });

    it('should fail a password missing a lowercase letter', () => {
        expect(isStrongPassword("STRONGPASS1")).toBe(false);
    });

    it('should fail a password missing an uppercase letter', () => {
        expect(isStrongPassword("strongpass1")).toBe(false);
    });

    it('should fail a password missing a number', () => {
        expect(isStrongPassword("StrongPassword")).toBe(false);
    });

    it('should fail a password that is too short', () => {
        expect(isStrongPassword("Short1")).toBe(false);
    });

    it('should validate a password that includes special characters but is still strong', () => {
        expect(isStrongPassword("Strong!Password1")).toBe(true);
    });
});
