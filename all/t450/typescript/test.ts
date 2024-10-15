describe('Password Validator Tests', () => {
    test('Valid password', () => {
        expect(isValidPassword("Password1!")).toBe(true);
    });

    test('Password without a number', () => {
        expect(isValidPassword("Password!")).toBe(false);
    });

    test('Password without an uppercase letter', () => {
        expect(isValidPassword("password1!")).toBe(false);
    });

    test('Password without a lowercase letter', () => {
        expect(isValidPassword("PASSWORD1!")).toBe(false);
    });

    test('Password without a punctuation mark', () => {
        expect(isValidPassword("Password1")).toBe(false);
    });

    test('Password shorter than 8 characters', () => {
        expect(isValidPassword("Pass1!")).toBe(false);
    });
});