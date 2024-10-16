describe('Count words in various strings', () => {
    test('Empty string', () => {
        expect(countWords("")).toBe(0);
    });

    test('String with only spaces', () => {
        expect(countWords("     ")).toBe(0);
    });

    test('Single word', () => {
        expect(countWords("Hello")).toBe(1);
    });

    test('Multiple words with single spaces', () => {
        expect(countWords("This is a test string")).toBe(5);
    });

    test('Multiple spaces between words', () => {
        expect(countWords("This    is   a   test   string")).toBe(5);
    });

    test('Leading and trailing spaces', () => {
        expect(countWords("   Hello world!   ")).toBe(2);
    });
});