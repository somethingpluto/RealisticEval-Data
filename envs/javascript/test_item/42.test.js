/**
 * Replaces all phone numbers in the string with the string [PHONE_NUM].
 * For example:
 *   input: "Call me at 123-456-7890."
 *   output: "Call me at [PHONE_NUM]."
 *
 * @param {string} text - The input string that may contain phone numbers.
 * @returns {string} The modified string with phone numbers replaced by '[PHONE_NUM]'.
 */
function replacePhoneNumbers(text) {
    // Regular expression to match phone numbers in various formats
    const phoneRegex = /\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b/g;
    // Replace all matches with [PHONE_NUM]
    return text.replace(phoneRegex, '[PHONE_NUM]');
}
describe('replacePhoneNumbers', () => {
    it('should replace a basic phone number', () => {
        const msg = "Call me at 123-456-7890.";
        const expected = "Call me at [PHONE_NUM].";
        expect(replacePhoneNumbers(msg)).toBe(expected);
    });

    it('should replace a phone number with parentheses', () => {
        const msg = "Our office number is 123 456-7890.";
        const expected = "Our office number is [PHONE_NUM].";
        expect(replacePhoneNumbers(msg)).toBe(expected);
    });

    it('should replace a phone number with dots', () => {
        const msg = "Fax us at 123.456.7890.";
        const expected = "Fax us at [PHONE_NUM].";
        expect(replacePhoneNumbers(msg)).toBe(expected);
    });

    it('should not replace text without a phone number', () => {
        const msg = "Hello, please reply to this email.";
        const expected = "Hello, please reply to this email.";
        expect(replacePhoneNumbers(msg)).toBe(expected);
    });
});
