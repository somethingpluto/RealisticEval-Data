/**
 * Removes the specified parameter from the URL query string.
 *
 * @param {string} url - The URL from which to remove the parameter.
 * @param {string} key - The key of the parameter to remove.
 * @returns {string} - The modified URL with the specified parameter removed.
 */
function removeQueryParam(url, key) {
    // Create an anchor element to parse the URL
    const anchor = document.createElement('a');
    anchor.href = url;

    // Get the query string and parse it into an object
    const queryParams = new URLSearchParams(anchor.search);

    // Remove the specified parameter
    queryParams.delete(key);

    // Update the anchor's search property with the modified query string
    anchor.search = queryParams.toString();

    // Return the modified URL
    return anchor.href;
}
describe('removeQueryParam', () => {
    test('should remove an existing parameter from the URL', () => {
        const url = 'https://example.com?page=1&sort=asc&filter=red';
        const result = removeQueryParam(url, 'sort');
        expect(result).toBe('https://example.com/?page=1&filter=red');
    });

    test('should not modify the URL if the parameter does not exist', () => {
        const url = 'https://example.com?page=1&filter=red';
        const result = removeQueryParam(url, 'sort');
        expect(result).toBe('https://example.com/?page=1&filter=red');
    });

    test('should return the original URL if there are no query parameters', () => {
        const url = 'https://example.com';
        const result = removeQueryParam(url, 'sort');
        expect(result).toBe('https://example.com/');
    });

    test('should remove multiple occurrences of a parameter', () => {
        const url = 'https://example.com?page=1&filter=red&filter=blue';
        const result = removeQueryParam(url, 'filter');
        expect(result).toBe('https://example.com/?page=1');
    });

    test('should handle encoded characters in the parameter', () => {
        const url = 'https://example.com?page=1&sort=asc&filter=hello%20world';
        const result = removeQueryParam(url, 'filter');
        expect(result).toBe('https://example.com/?page=1&sort=asc');
    });

    test('should handle the case when the parameter is the only one in the URL', () => {
        const url = 'https://example.com?sort=asc';
        const result = removeQueryParam(url, 'sort');
        expect(result).toBe('https://example.com/');
    });
});
