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