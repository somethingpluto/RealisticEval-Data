describe('toQueryString', () => {
    test('should return an empty string for an empty object', () => {
        const params = {};
        const result = toQueryString(params);
        expect(result).toBe('');
    });

    test('should convert a simple object to a query string', () => {
        const params = { search: 'test', page: 1, size: 10 };
        const result = toQueryString(params);
        expect(result).toBe('?search=test&page=1&size=10');
    });

    test('should ignore null and undefined values', () => {
        const params = { search: 'test', page: null, size: undefined, sort: 'asc' };
        const result = toQueryString(params);
        expect(result).toBe('?search=test&sort=asc');
    });

    test('should encode special characters in the query string', () => {
        const params = { search: 'hello world', filter: 'price < \$50' };
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