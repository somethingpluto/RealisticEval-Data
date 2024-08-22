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
/**
 * Validates a URL string using a simplified and more comprehensive regular expression.
 *
 * @param {string} str - The URL string to validate.
 * @returns {boolean} True if the URL is valid, false otherwise.
 */
function validURL(str) {
    // Simplified and robust regex for URL validation
    const pattern = new RegExp('^(http|https?:\\/\\/)?' + // protocol
        '((([a-zA-Z\\d]([a-zA-Z\\d-]*[a-zA-Z\\d])*)\\.)+[a-zA-Z]{2,}|' + // domain name and extension
        '((\\d{1,3}\\.){3}\\d{1,3}))' + // OR ip (v4) address
        '(\\:\\d+)?' + // port
        '(\\/[-a-zA-Z\\d%_.~+]*)*' + // path
        '(\\?[;&amp;a-zA-Z\\d%_.~+=-]*)?' + // query string
        '(\\#[-a-zA-Z\\d_]*)?$', 'i'); // fragment locator
    return !!pattern.test(str);
}
