/**
 * Check if the given text contains an email address.
 *
 * @param {string} text - The string to search for an email address.
 * @returns {boolean} - True if an email address is found, False otherwise.
 */
function containsEmail(text) {
    // Regular expression to match a basic email address pattern
    const emailRegex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/;
    
    // Test the text against the regex
    return emailRegex.test(text);
}
describe('TestContainsEmail', () => {
    describe('Testing email detection', () => {
        it('should detect a valid email in the string', () => {
            const testString = "You can reach me at example@example.com for more info.";
            expect(containsEmail(testString)).toBe(true);
        });

        it('should detect an email with special characters', () => {
            const testString = "My email address is john.doe123+test@gmail.com!";
            expect(containsEmail(testString)).toBe(true);
        });

        it('should not detect an email in a string without emails', () => {
            const testString = "This string does not have an email.";
            expect(containsEmail(testString)).toBe(false);
        });

        it('should detect multiple emails in a string', () => {
            const testString = "You can contact me at example1@example.com or example2@example.com.";
            expect(containsEmail(testString)).toBe(true);
        });

        it('should not detect an email with an invalid format', () => {
            const testString = "Please contact me at example@.com or test@domain.";
            expect(containsEmail(testString)).toBe(false);
        });
    });
});
