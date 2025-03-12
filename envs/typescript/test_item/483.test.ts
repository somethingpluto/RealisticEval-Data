import { validate } from 'email-validator';

/**
 * Verifies if the provided string is a valid email address.
 * 
 * @param email - The email address to validate.
 * @returns True if the email address is valid, False otherwise.
 */
function isValidEmail(email: string): boolean {
  return validate(email);
}
describe('Email Validation', () => {
    it('should validate a valid email', () => {
        expect(isValidEmail('test@example.com')).toBe(true);
    });

    it('should validate a valid email with subdomain', () => {
        expect(isValidEmail('user@subdomain.example.com')).toBe(true);
    });

    it('should validate a valid email with plus tag', () => {
        expect(isValidEmail('user.name+tag+sorting@example.com')).toBe(true);
    });

    it('should invalidate an email missing username', () => {
        expect(isValidEmail('@missingusername.com')).toBe(false);
    });

    it('should invalidate an email missing at symbol', () => {
        expect(isValidEmail('missingatsign.com')).toBe(false);
    });

    it('should invalidate an email with too short TLD', () => {
        expect(isValidEmail('user@domain.c')).toBe(false);
    });

    it('should invalidate an email with special characters', () => {
        expect(isValidEmail('user@domain.com!')).toBe(false);
    });
});
