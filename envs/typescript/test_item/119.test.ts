// Assuming the start of the file with necessary imports
import { parseCookies } from 'cookie'; // Import the parseCookies function from the 'cookie' library

function getCookie(name: string): string | null {
  const cookies = document.cookie.split(';');
  const cookieName = `${name}=`;
  for (let cookie of cookies) {
    let cookiePair = cookie.trim().split('=');
    if (cookiePair[0].startsWith(cookieName)) {
      return decodeURIComponent(cookiePair[1]);
    }
  }
  return null;
}

// Assuming the end of the file
describe('getCookie function tests', () => {
    beforeEach(() => {
        // Clear cookies before each test
        Object.defineProperty(window.document, 'cookie', {
            writable: true,
            value: '',
        });
    });

    test('returns correct cookie value for existing cookie', () => {
        document.cookie = "username=JohnDoe; expires=Thu, 18 Dec 2023 12:00:00 UTC; path=/";
        expect(getCookie('username')).toBe('JohnDoe');
    });

    test('returns null if cookie does not exist', () => {
        document.cookie = "username=JohnDoe; expires=Thu, 18 Dec 2023 12:00:00 UTC; path=/";
        expect(getCookie('user')).toBeNull();
    });

    test('returns null when no cookies are set', () => {
        expect(getCookie('username')).toBeNull();
    });

    test('handles multiple cookies and retrieves the correct one', () => {
        document.cookie = "user=JaneDoe; expires=Thu, 18 Dec 2023 12:00:00 UTC; path=/";
        document.cookie = "username=JohnDoe; expires=Thu, 18 Dec 2023 12:00:00 UTC; path=/";
        expect(getCookie('username')).toBe('JohnDoe');
    });
});
