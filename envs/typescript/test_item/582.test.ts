// Start of the code context
import { URLSearchParams } from 'url';

function toQueryString(params: Record<string, any>): string {
  const searchParams = new URLSearchParams();
  for (const key in params) {
    if (params.hasOwnProperty(key)) {
      const value = params[key];
      if (Array.isArray(value)) {
        value.forEach((item) => {
          searchParams.append(key, item.toString());
        });
      } else {
        searchParams.append(key, value.toString());
      }
    }
  }
  return searchParams.toString();
}
// End of the code context
describe('toQueryString', () => {

    test('should convert a simple object to a query string', () => {
        const params = {search: 'test', page: 1, size: 10};
        const result = toQueryString(params);
        expect(result).toBe('?search=test&page=1&size=10');
    });


    test('should encode special characters in the query string', () => {
        const params = {search: 'hello world', filter: 'price < \$50'};
        const result = toQueryString(params);
        expect(result).toBe('?search=hello%20world&filter=price%20%3C%20%2450');
    });

    test('should handle empty string values', () => {
        const params = {search: '', page: 1};
        const result = toQueryString(params);
        expect(result).toBe('?search=&page=1');
    });

    test('should handle boolean values', () => {
        const params = {isActive: true, isVerified: false};
        const result = toQueryString(params);
        expect(result).toBe('?isActive=true&isVerified=false');
    });
});

