/**
 * Determines whether the string contains a phone number. Possible formats for a phone number include +1-800-555-1234, 555-555-1234, and 555 555 1234.
 * @param {string} s - The input string that may contain a phone number.
 * @returns {boolean} - Whether the string contains a phone number.
 */
function containsPhoneNumber(s) {
    const phoneNumberRegex = /^(?:\+1\s?)?(?:\(\d{3}\)|\d{3})[\s-]?\d{3}[\s-]?\d{4}$/;
    return phoneNumberRegex.test(s);
}
describe('TestPhoneNumberDetection', () => {
    it('should detect international prefix', () => {
        expect(containsPhoneNumber('+1-800-555-1234')).toBe(true);
    });

    it('should detect standard format with dashes', () => {
        expect(containsPhoneNumber('800-555-1234')).toBe(true);
    });

    it('should detect standard format with spaces', () => {
        expect(containsPhoneNumber('800 555 1234')).toBe(true);
    });

    it('should not detect any phone number', () => {
        expect(containsPhoneNumber('Hello, world!')).toBe(false);
    });

    it('should detect phone number in text', () => {
        expect(containsPhoneNumber('Call me at 800-555-1234 today!')).toBe(true);
    });
});
