// ... (previous code for context)

function extractEmailDetails(email: string): [string, string] {
  const [username, domain] = email.split('@');
  return [username, domain];
}

// Unit tests
describe('extractEmailDetails', () => {
  it('should return the correct username and domain', () => {
    expect(extractEmailDetails('xxx@gmail.com')).toEqual(['xxx', 'gmail.com']);
  });

  it('should handle emails with subdomains', () => {
    expect(extractEmailDetails('xxx@sub.domain.com')).toEqual(['xxx', 'sub.domain.com']);
  });

  it('should handle emails with country code top-level domains', () => {
    expect(extractEmailDetails('xxx@domain.co.uk')).toEqual(['xxx', 'domain.co.uk']);
  });
});

// ... (rest of the code)
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
