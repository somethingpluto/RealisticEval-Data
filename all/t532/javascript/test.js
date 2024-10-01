describe('countLetterChanges', () => {
    test('should count consecutive letters correctly', () => {
        const result = countLetterChanges("aaabbcdeee");
        expect(result).toEqual([3, 2, 1, 1, 3]);
    });

    test('should return an array with one count for a single character', () => {
        const result = countLetterChanges("a");
        expect(result).toEqual([1]);
    });

    test('should return counts for a string with no consecutive letters', () => {
        const result = countLetterChanges("abcdef");
        expect(result).toEqual([1, 1, 1, 1, 1, 1]);
    });

    test('should handle a string with only identical letters', () => {
        const result = countLetterChanges("rrrrrr");
        expect(result).toEqual([6]);
    });

    test('should handle a long string with random letters', () => {
        const result = countLetterChanges("xxxyyyzzzaaaab");
        expect(result).toEqual([3, 3, 3, 4, 1]);
    });

    test('should handle numeric characters in the string', () => {
        const result = countLetterChanges("1122334455");
        expect(result).toEqual([2, 2, 2, 2, 2]);
    });
});