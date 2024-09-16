describe('removePunctuation', () => {
    test('removes punctuation from a simple sentence', () => {
        const input = "Hello, world!";
        const expected = "hello world";
        expect(removePunctuation(input)).toBe(expected);
    });

    test('handles a string with no punctuation', () => {
        const input = "Hello world";
        const expected = "hello world";
        expect(removePunctuation(input)).toBe(expected);
    });

    test('converts mixed case letters to lowercase', () => {
        const input = "HeLLo WoRLd!";
        const expected = "hello world";
        expect(removePunctuation(input)).toBe(expected);
    });

    test('removes a variety of punctuation', () => {
        const input = "Life, in a nutshell: eat, sleep, code!";
        const expected = "life in a nutshell eat sleep code";
        expect(removePunctuation(input)).toBe(expected);
    });

    test('trims whitespace from the ends of the string', () => {
        const input = "   What a wonderful world!   ";
        const expected = "what a wonderful world";
        expect(removePunctuation(input)).toBe(expected);
    });
});