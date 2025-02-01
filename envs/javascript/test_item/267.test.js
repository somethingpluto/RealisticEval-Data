/**
 * Extracts the second-level domain (SLD) and top-level domain (TLD) from a fully qualified domain name (FQDN).
 * 
 * @param {string} fqdn - The fully qualified domain name.
 * @returns {Array<string>} An array containing the second-level domain and top-level domain.
 */
function extractSldTld(fqdn) {
    const parts = fqdn.split('.');
    if (parts.length < 2) {
        throw new Error('Invalid FQDN');
    }
    const sld = parts[parts.length - 2];
    const tld = parts[parts.length - 1];
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
