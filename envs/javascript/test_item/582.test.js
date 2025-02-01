/**
 * Converts an object to a query string.
 * For example:
 *      input: { search: 'test', page: 1, size: 10 };
 *      output: ?search=test&page=1&size=10
 *
 * @param {Object} params - The parameters to convert.
 * @returns {string} - The query string.
 */
function toQueryString(params) {
    return Object.keys(params)
        .map(key => encodeURIComponent(key) + '=' + encodeURIComponent(params[key]))
        .join('&')
        .replace(/^&/, '?');
}
describe('toQueryString', () => {

    test('should convert a simple object to a query string', () => {
        const params = { search: 'test', page: 1, size: 10 };
        const result = toQueryString(params);
        expect(result).toBe('?search=test&page=1&size=10');
    });

    test('should encode special characters in the query string', () => {
        const params = { search: 'hello world', filter: 'price < $50' };
        const result = toQueryString(params);
        expect(result).toBe('?search=hello%20world&filter=price%20%3C%20%2450');
    });

    test('should handle empty string values', () => {
        const params = { search: '', page: 1 };
        const result = toQueryString(params);
        expect(result).toBe('?search=&page=1');
    });

    test('should handle boolean values', () => {
        const params = { isActive: true, isVerified: false };
        const result = toQueryString(params);
        expect(result).toBe('?isActive=true&isVerified=false');
    });
});
