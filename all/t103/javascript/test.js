describe('sliceString Function Tests', () => {
    test('should return a truncated string with "..." if it is longer than the specified limit, containing <p> tags', () => {
        expect(sliceString("<p>Hello, World!</p>", 5)).toBe("He...");
    });

    test('should return the original string if it is exactly at the specified limit', () => {
        expect(sliceString("Hello", 5)).toBe("Hello");
    });

    test('should return the original string if it is shorter than the specified limit', () => {
        expect(sliceString("Hi", 5)).toBe("Hi");
    });

    test('should return a truncated string with "..." if it is longer than the specified limit, without <p> tags', () => {
        expect(sliceString("Hello, World!", 8)).toBe("Hello, W...");
    });

    test('should return a truncated string with "..." if it has multiple <p> tags and is longer than the specified limit', () => {
        expect(sliceString("<p>Hello, <p>World!</p></p>", 7)).toBe("Hello, ...");
    });
});