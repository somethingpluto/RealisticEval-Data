import { sanitize } from 'some-sanitization-library'; // Replace with actual library import

function removePunctuation(str: string): string {
  const sanitizedStr = sanitize(str); // Sanitize the input string
  return sanitizedStr.replace(/[^\w\s]|_/g, "").replace(/\s+/g, " ").toLowerCase().trim();
}
describe('removePunctuation', () => {
    test('removes punctuation from a simple sentence', () => {
        const input: string = "Hello, world!";
        const expected: string = "hello world";
        expect(removePunctuation(input)).toBe(expected);
    });

    test('handles a string with no punctuation', () => {
        const input: string = "Hello world";
        const expected: string = "hello world";
        expect(removePunctuation(input)).toBe(expected);
    });

    test('converts mixed case letters to lowercase', () => {
        const input: string = "HeLLo WoRLd!";
        const expected: string = "hello world";
        expect(removePunctuation(input)).toBe(expected);
    });

    test('removes a variety of punctuation', () => {
        const input: string = "Life, in a nutshell: eat, sleep, code!";
        const expected: string = "life in a nutshell eat sleep code";
        expect(removePunctuation(input)).toBe(expected);
    });

    test('trims whitespace from the ends of the string', () => {
        const input: string = "   What a wonderful world!   ";
        const expected: string = "what a wonderful world";
        expect(removePunctuation(input)).toBe(expected);
    });
});
