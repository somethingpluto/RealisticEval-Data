/**
 * @jest-environment jsdom
 */

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

    test('correctly handles cookies with spaces before names', () => {
        document.cookie = " username=JohnDoe; expires=Thu, 18 Dec 2023 12:00:00 UTC; path=/";
        expect(getCookie('username')).toBe('JohnDoe');
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
function getCookie(name) {
    let cookieName = `${name}=`;
    let cookies = document.cookie.split(';').map(cookie => cookie.trim()); // Trim whitespace once
    for (let cookie of cookies) {
        if (cookie.startsWith(cookieName)) {
            return cookie.substring(cookieName.length);
        }
    }
    return null; // Typically, returning null is more appropriate for not found
}