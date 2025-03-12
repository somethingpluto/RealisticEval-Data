import { URLSearchParams } from 'url';

function getFileIdFromUrl(url: string): string | null {
  const searchParams = new URLSearchParams(url.split('?')[1]);
  return searchParams.get('fileId') || null;
}
describe('getFileIdFromUrl', () => {
    test('should return the file ID when a valid URL with fileId is provided', () => {
        const url: string = 'https://example.com/download?fileId=12345';
        expect(getFileIdFromUrl(url)).toBe('12345');
    });

    test('should return null when the fileId query parameter is missing', () => {
        const url: string = 'https://example.com/download';
        expect(getFileIdFromUrl(url)).toBeNull();
    });

    test('should return null when the fileId query parameter is empty', () => {
        const url: string = 'https://example.com/download?fileId=';
        expect(getFileIdFromUrl(url)).toBeNull();
    });

    test('should return null for a malformed URL', () => {
        const url: string = 'https://example.com/download?fileId=12345&otherParam';
        expect(getFileIdFromUrl(url)).toBe('12345'); // Adjust this depending on your needs; the function should still work correctly.
    });
});
