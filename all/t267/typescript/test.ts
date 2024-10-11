describe('extract_sld_tld', () => {
  it('should correctly extract SLD and TLD from a valid FQDN', () => {
    const fqdn = 'example.com';
    const [sld, tld] = extract_sld_tld(fqdn);
    expect(sld).toBe('example');
    expect(tld).toBe('com');
  });

  it('should handle multiple levels of subdomains', () => {
    const fqdn = 'sub.example.co.uk';
    const [sld, tld] = extract_sld_tld(fqdn);
    expect(sld).toBe('example');
    expect(tld).toBe('co.uk');
  });

  it('should handle hyphenated domains', () => {
    const fqdn = 'my-domain.com';
    const [sld, tld] = extract_sld_tld(fqdn);
    expect(sld).toBe('my-domain');
    expect(tld).toBe('com');
  });

  it('should handle internationalized domains', () => {
    const fqdn = 'xn--exmpl-1ga.com';
    const [sld, tld] = extract_sld_tld(fqdn);
    expect(sld).toBe('exmpl');
    expect(tld).toBe('com');
  });

  it('should throw an error for invalid FQDNs', () => {
    expect(() => extract_sld_tld('invalid')).toThrowError();
  });
});