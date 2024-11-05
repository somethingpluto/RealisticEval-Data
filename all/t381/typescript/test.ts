describe('TestExtractEmailDetails', () => {
    it('test_valid_email', () => {
        // Test with a typical email address
        const email = "user@example.com";
        const expected = ["user", "example.com"];
        const result = extractEmailDetails(email);
        expect(result).toEqual(expected);
    });

    it('test_valid_email_with_subdomain', () => {
        // Test with an email that includes a subdomain
        const email = "user@mail.office.com";
        const expected = ["user", "mail.office.com"];
        const result = extractEmailDetails(email);
        expect(result).toEqual(expected);
    });

    it('test_email_without_at_symbol', () => {
        // Test with an email that lacks an '@' symbol
        const email = "userexample.com";
        expect(() => extractEmailDetails(email)).toThrowError("Invalid email address. Email must contain an '@' character.");
    });

    it('test_empty_email', () => {
        // Test with an empty string as an email
        const email = "";
        expect(() => extractEmailDetails(email)).toThrowError("Invalid email address. Email must contain an '@' character.");
    });
});