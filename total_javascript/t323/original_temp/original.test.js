describe('isValidUsername', () => {
    test('should return true for a valid username with letters, numbers, and underscores', () => {
        const result = isValidUsername('user_123');
        expect(result).toBe(true); // 'user_123' is a valid username
    });

    test('should return true for a valid username with only letters', () => {
        const result = isValidUsername('username');
        expect(result).toBe(true); // 'username' is a valid username
    });

    test('should return false for a username with special characters', () => {
        const result = isValidUsername('user-name');
        expect(result).toBe(false); // 'user-name' contains a hyphen
    });

    test('should return false for a username with spaces', () => {
        const result = isValidUsername('user name');
        expect(result).toBe(false); // 'user name' contains spaces
    });

    test('should return true for a valid username with only numbers', () => {
        const result = isValidUsername('12345');
        expect(result).toBe(true); // '12345' is a valid username
    });
});

// Generated using ChatGPT
function isValidUsername(uname) {
    const re = /^[a-zA-Z0-9_]+$/;
    return re.test(uname);
}