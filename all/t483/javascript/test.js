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

    it('should invalidate an email with TLD too short', () => {
        expect(isValidEmail('user@domain.c')).toBe(false);
    });

    it('should invalidate an email with special characters', () => {
        expect(isValidEmail('user@domain.com!')).toBe(false);
    });
});