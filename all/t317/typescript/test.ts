describe('countLetters', () => {
    test('should return 10 for the string "Hello, World!"', () => {
        expect(countLetters("Hello, World!")).toBe(10);
    });

    test('should return 0 for a string with no letters "12345"', () => {
        expect(countLetters("12345")).toBe(0);
    });

    test('should return 6 for the string "abc 123 xyz!"', () => {
        expect(countLetters("abc 123 xyz!")).toBe(6);
    });

    test('should return 0 for an empty string', () => {
        expect(countLetters("")).toBe(0);
    });

    test('should return 3 for the string "A1B2C3!@#"', () => {
        expect(countLetters("A1B2C3!@#")).toBe(3);
    });

    test('should return 5 for a string with mixed case "AbCdE"', () => {
        expect(countLetters("AbCdE")).toBe(5);
    });
});