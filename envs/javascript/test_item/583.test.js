/**
 * Removes the specified parameter from the URL query string.
 *
 * @param {string} url - The URL from which to remove the parameter.
 * @param {string} key - The key of the parameter to remove.
 * @returns {string} - The modified URL with the specified parameter removed.
 */
function removeQueryParam(url, key) {
    // Create a URL object to easily manipulate the URL
    const urlObj = new URL(url);
    
    // Remove the specified query parameter
    urlObj.searchParams.delete(key);
    
    // Return the modified URL as a string
    return urlObj.toString();
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
