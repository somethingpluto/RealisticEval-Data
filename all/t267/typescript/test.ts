describe('TestExtractSldTld', () => {
  it('test standard FQDN', () => {
      // Test a typical FQDN
      expect(extractSldTld("www.example.com")).toEqual(["example", "com"]);
  });

  it('test standard FQDN2', () => {
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