function containsEmail(text: string): boolean {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(text);
}
describe('TestContainsEmail', () => {
    it('test_contains_valid_email', () => {
        // Test if a valid email is detected in the string.
        const testString = "You can reach me at example@example.com for more info.";
        expect(containsEmail(testString)).toBe(true);
    });

    it('test_contains_email_with_special_characters', () => {
        // Test if an email with special characters is detected.
        const testString = "My email address is john.doe123+test@gmail.com!";
        expect(containsEmail(testString)).toBe(true);
    });

    it('test_does_not_contain_email', () => {
        // Test a string that does not contain any email address.
        const testString = "This string does not have an email.";
        expect(containsEmail(testString)).toBe(false);
    });

    it('test_contains_multiple_emails', () => {
        // Test a string containing multiple email addresses.
        const testString = "You can contact me at example1@example.com or example2@example.com.";
        expect(containsEmail(testString)).toBe(true);
    });

    it('test_contains_invalid_email_format', () => {
        // Test a string with an invalid email format.
        const testString = "Please contact me at example@.com or test@domain.";
        expect(containsEmail(testString)).toBe(false);
    });
});
