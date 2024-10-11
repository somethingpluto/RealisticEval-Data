describe('extractSldTld', () => {
    it('should correctly extract SLD and TLD from valid FQDN', () => {
        expect(extractSldTld('example.com')).toEqual(['example', 'com']);
        expect(extractSldTld('subdomain.example.co.uk')).toEqual(['subdomain.example', 'co.uk']);
    });

    it('should handle multiple levels of subdomains', () => {
        expect(extractSldTld('level1.level2.subdomain.example.net')).toEqual(['level1.level2.subdomain', 'example.net']);
    });

    it('should handle special characters in TLD', () => {
        expect(extractSldTld('special.tld-example.org')).toEqual(['special.tld-example', 'org']);
    });

    it('should throw an error for invalid FQDN', () => {
        expect(() => extractSldTld('invalid')).toThrowError('Invalid FQDN');
    });
});