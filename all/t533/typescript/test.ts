describe('shuffleString', () => {
    test('should return a string of the same length as the input', () => {
        const input: string = "abcdef";
        const result: string = shuffleString(input);
        expect(result.length).toBe(input.length);
    });

    test('should shuffle the characters in the string', () => {
        const input: string = "hello";
        const result: string = shuffleString(input);
        expect(result).not.toBe(input); // It should be different most of the time
    });

    test('should return an empty string when given an empty string', () => {
        const input: string = "";
        const result: string = shuffleString(input);
        expect(result).toBe(""); // Should return an empty string
    });

    test('should handle a single character string', () => {
        const input: string = "a";
        const result: string = shuffleString(input);
        expect(result).toBe("a"); // Should return the same single character
    });

    test('should handle strings with identical characters', () => {
        const input: string = "aaaaa";
        const result: string = shuffleString(input);
        expect(result).toBe("aaaaa"); // Should return the same string
    });

    test('should return a shuffled string for longer strings', () => {
        const input: string = "abcdefghijklmnopqrstuvwxyz";
        const result: string = shuffleString(input);
        expect(result).not.toBe(input); // It should be different most of the time
        expect(result.length).toBe(input.length); // Length should be the same
    });

    test('should return the same string if all characters are the same', () => {
        const input: string = "111111";
        const result: string = shuffleString(input);
        expect(result).toBe("111111"); // Should return the same string
    });

    test('should shuffle a string containing special characters', () => {
        const input: string = "a!@#$%^&*()_+";
        const result: string = shuffleString(input);
        expect(result.length).toBe(input.length); // Length should be the same
        expect(result).not.toBe(input); // It should be different most of the time
    });
});