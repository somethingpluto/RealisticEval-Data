describe('shuffleString', () => {
    test('should return a string of the same length as the input', () => {
        const input = "abcdef";
        const result = shuffleString(input);
        expect(result.length).toBe(input.length);
    });

    test('should shuffle the characters in the string', () => {
        const input = "hello";
        const result = shuffleString(input);
        expect(result).not.toBe(input); // It should be different most of the time
    });

    test('should return an empty string when given an empty string', () => {
        const input = "";
        const result = shuffleString(input);
        expect(result).toBe(""); // Should return an empty string
    });

    test('should handle a single character string', () => {
        const input = "a";
        const result = shuffleString(input);
        expect(result).toBe("a"); // Should return the same single character
    });

    test('should handle strings with identical characters', () => {
        const input = "aaaaa";
        const result = shuffleString(input);
        expect(result).toBe("aaaaa"); // Should return the same string
    });

    test('should return a shuffled string for longer strings', () => {
        const input = "abcdefghijklmnopqrstuvwxyz";
        const result = shuffleString(input);
        expect(result).not.toBe(input); // It should be different most of the time
        expect(result.length).toBe(input.length); // Length should be the same
    });

    test('should return the same string if all characters are the same', () => {
        const input = "111111";
        const result = shuffleString(input);
        expect(result).toBe("111111"); // Should return the same string
    });

    test('should shuffle a string containing special characters', () => {
        const input = "a!@#$%^&*()_+";
        const result = shuffleString(input);
        expect(result.length).toBe(input.length); // Length should be the same
        expect(result).not.toBe(input); // It should be different most of the time
    });
});