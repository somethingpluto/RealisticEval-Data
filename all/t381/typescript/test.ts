describe('extractEmailDetails', () => {
    it('should extract details from a typical email address', () => {
        const email = 'user@example.com';
        const expected = ['user', 'example.com'];
        const result = extractEmailDetails(email);
        expect(result).toEqual(expected);
    });

    it('should extract details from an email with a subdomain', () => {
        const email = 'user@mail.office.com';
        const expected = ['user', 'mail.office.com'];
        const result = extractEmailDetails(email);
        expect(result).toEqual(expected);
    });

    it('should throw an error for an email without an @ symbol', () => {
        const email = 'userexample.com';
        expect(() => extractEmailDetails(email)).toThrow('Invalid email address. Email must contain an \'@\' character.');
    });

    it('should throw an error for an empty email', () => {
        const email = '';
        expect(() => extractEmailDetails(email)).toThrow('Invalid email address. Email must contain an \'@\' character.');
    });
});