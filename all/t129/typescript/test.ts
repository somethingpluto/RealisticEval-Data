describe('validURL', () => {
    test('validates a standard HTTP URL', () => {
        const url: string = 'http://www.example.com';
        expect(validURL(url)).toBe(true);
    });

    test('validates a secure HTTPS URL', () => {
        const url: string = 'https://www.example.com';
        expect(validURL(url)).toBe(true);
    });

    test('rejects a malformed URL', () => {
        const url: string = 'htp:/www.example.com';
        expect(validURL(url)).toBe(false);
    });
});