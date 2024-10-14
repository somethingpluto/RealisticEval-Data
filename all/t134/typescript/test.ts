describe('isValidUsername', () => {
    test('valid username with alphanumeric characters', () => {
        expect(isValidUsername('User123')).toBe(true);
    });

    test('valid username with spaces', () => {
        expect(isValidUsername('User 123')).toBe(true);
    });

    test('invalid username that is too short', () => {
        expect(isValidUsername('User')).toBe(false);
    });

    test('invalid username that is too long', () => {
        expect(isValidUsername('ThisIsAVeryLongUsername')).toBe(false);
    });

    test('invalid username with special characters', () => {
        expect(isValidUsername('User!')).toBe(false);
    });

    test('invalid username with only spaces', () => {
        expect(isValidUsername('     ')).toBe(false);
    });

    test('invalid input type (number)', () => {
        expect(isValidUsername(12345 as any)).toBe(false); // Using 'as any' to bypass type check
    });
});