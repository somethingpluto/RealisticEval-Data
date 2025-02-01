/**
 * @jest-environment jsdom
 *//**
 * gets the cookie value for the specified name from the cookie in the browser. The format of the cookie is key=value;key=value;key=value
 * @param name cookie key name
 */
function getCookie(name) {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith(name + '=')) {
            return cookie.substring(name.length + 1);
        }
    }
    return null;
}
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

    test('returns undefined if cookie does not exist', () => {
        document.cookie = "username=JohnDoe; expires=Thu, 18 Dec 2023 12:00:00 UTC; path=/";
        expect(getCookie('user')).toBeFalsy();
    });


    test('returns undefined when no cookies are set', () => {
        expect(getCookie('username')).toBeFalsy();
    });

    test('handles multiple cookies and retrieves the correct one', () => {
        document.cookie = "user=JaneDoe; expires=Thu, 18 Dec 2023 12:00:00 UTC; path=/";
        document.cookie = "username=JohnDoe; expires=Thu, 18 Dec 2023 12:00:00 UTC; path=/";
        expect(getCookie('username')).toBe('JohnDoe');
    });
});

