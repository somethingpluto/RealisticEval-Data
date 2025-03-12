/**
 * @jest-environment jsdom
 *//**
 * Gets the cookie value for the specified name from the cookie in the browser. The format of the cookie is key=value;key=value;key=value
 * @param name cookie key name
 */
function getCookie(name) {
    // Split the cookie string into an array of key=value pairs
    const cookies = document.cookie.split(';');

    // Iterate through the array to find the specified cookie name
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i].trim();

        // Check if the cookie starts with the specified name
        if (cookie.indexOf(name + '=') === 0) {
            // Return the value part of the cookie
            return cookie.substring(name.length + 1);
        }
    }

    // Return null if the cookie is not found
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

