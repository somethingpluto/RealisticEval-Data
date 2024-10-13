describe('containsPhoneNumber', () => {
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