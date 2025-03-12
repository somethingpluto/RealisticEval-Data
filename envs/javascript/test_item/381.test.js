/**
 * Extracts the username and mailbox suffix from an email address.
 * Example: extractEmailDetails("xxx@gmail.com") returns ['xxx', 'gmail.com']
 * 
 * @param {string} email - The email address to extract details from.
 * @returns {Array} An array [username, domain] where:
 *      username is the part before '@'
 *      domain is the part after '@'
 */
function extractEmailDetails(email) {
    // Split the email address at the '@' symbol
    const parts = email.split('@');

    // Extract the username and domain
    const username = parts[0];
    const domain = parts[1];

    // Return the result as an array
    return [username, domain];
}
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
