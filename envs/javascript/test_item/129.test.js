/**
 * Validates a URL string using a simplified and more comprehensive regular expression.
 *
 * @param {string} str - The URL string to validate.
 * @returns {boolean} True if the URL is valid, false otherwise.
 */
function validURL(str) {
    const pattern = new RegExp(
        '^(https?:\\/\\/)?' + // protocol
        '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' + // domain name
        '((\\d{1,3}\\.){3}\\d{1,3}))' + // OR ip (v4) address
        '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' + // port and path
        '(\\?[;&a-z\\d%_.~+=-]*)?' + // query string
        '(\\#[-a-z\\d_]*)?$', 'i' // fragment locator
    );
    return !!pattern.test(str);
}
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
