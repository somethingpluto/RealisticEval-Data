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
        expect(getCookie('user')).toBeUndefined();
    });


    test('returns undefined when no cookies are set', () => {
        expect(getCookie('username')).toBeUndefined();
    });

    test('handles multiple cookies and retrieves the correct one', () => {
        document.cookie = "user=JaneDoe; expires=Thu, 18 Dec 2023 12:00:00 UTC; path=/";
        document.cookie = "username=JohnDoe; expires=Thu, 18 Dec 2023 12:00:00 UTC; path=/";
        expect(getCookie('username')).toBe('JohnDoe');
    });
});