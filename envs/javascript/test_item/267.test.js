/**
 * Extracts the second-level domain (SLD) and top-level domain (TLD) from a fully qualified domain name (FQDN).
 * 
 * @param {string} fqdn - The fully qualified domain name.
 * @returns {Array<string>} An array containing the second-level domain and top-level domain.
 */
function extractSldTld(fqdn) {
    // Split the FQDN by dots
    const parts = fqdn.split('.');

    // The TLD is the last part
    const tld = parts.pop();

    // The SLD is the second last part
    const sld = parts.pop();

    // Return the SLD and TLD as an array
    return [sld, tld];
}
describe('TestExtractSldTld', () => {
    it('test standard FQDN', () => {
        // Test a typical FQDN
        expect(extractSldTld("www.example.com")).toEqual(["example", "com"]);
    });

    it('test standard FQDN 2', () => {
        // Test a typical FQDN
        expect(extractSldTld("www.example.xyz")).toEqual(["example", "xyz"]);
    });

    it('test FQDN with subdomains', () => {
        // Test an FQDN with multiple subdomains
        expect(extractSldTld("blog.subdomain.example.com")).toEqual(["example", "com"]);
    });

    it('test numeric TLD', () => {
        // Test a numeric TLD, which can occur in private networks
        expect(extractSldTld("server.example.123")).toEqual(["example", "123"]);
    });
});
