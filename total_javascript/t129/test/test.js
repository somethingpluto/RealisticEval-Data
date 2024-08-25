describe('validURL', () => {
    test('validates a standard HTTP URL', () => {
        const url = 'http://www.example.com';
        expect(validURL(url)).toBe(true);
    });

    test('validates a secure HTTPS URL', () => {
        const url = 'https://www.example.com';
        expect(validURL(url)).toBe(true);
    });

    test('rejects a malformed URL', () => {
        const url = 'htp:/www.example.com';
        expect(validURL(url)).toBe(false);
    });

    test('validates a URL with IP address and query parameters', () => {
        const url = 'http://192.168.1.1:8080/search?query=test';
        expect(validURL(url)).toBe(true);
    });
});