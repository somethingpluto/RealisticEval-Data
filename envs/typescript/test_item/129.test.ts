import { URL } from 'url';

function validURL(str: string): boolean {
  try {
    const url = new URL(str);
    return url.hostname && url.protocol;
  } catch (_) {
    return false;
  }
}
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
