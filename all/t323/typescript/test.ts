describe('isValidUsername', () => {
    test('should return true for a valid username with letters, numbers, and underscores', () => {
        const result: boolean = isValidUsername('user_123');
        expect(result).toBe(true); // 'user_123' is a valid username
    });

    test('should return true for a valid username with only letters', () => {
        const result: boolean = isValidUsername('username');
        expect(result).toBe(true); // 'username' is a valid username
    });

    test('should return false for a username with special characters', () => {
        const result: boolean = isValidUsername('user-name');
        expect(result).toBe(false); // 'user-name' contains a hyphen
    });

    test('should return false for a username with spaces', () => {
        const result: boolean = isValidUsername('user name');
        expect(result).toBe(false); // 'user name' contains spaces
    });

    test('should return true for a valid username with only numbers', () => {
        const result: boolean = isValidUsername('12345');
        expect(result).toBe(true); // '12345' is a valid username
    });
});