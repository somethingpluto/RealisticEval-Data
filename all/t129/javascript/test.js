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
});