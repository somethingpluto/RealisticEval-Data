// ... (previous code for context)
function countLetterChanges(inputString: string): number[] {
    if (!inputString) {
        return [];
    }
    // ... (rest of the function)
}

// Unit tests
describe('countLetterChanges', () => {
    it('should return an empty array for an empty string', () => {
        expect(countLetterChanges('')).toEqual([]);
    });

    it('should return an array with one element for a single character string', () => {
        expect(countLetterChanges('a')).toEqual([1]);
    });

    it('should handle strings with no letter changes', () => {
        expect(countLetterChanges('aaaaa')).toEqual([5]);
    });

    it('should handle strings with multiple letter changes', () => {
        expect(countLetterChanges('aabbcc')).toEqual([2, 2, 2]);
    });

    it('should handle strings with mixed case letters', () => {
        expect(countLetterChanges('AaAa')).toEqual([1, 1, 1, 1]);
    });

    it('should handle strings with special characters and numbers', () => {
        expect(countLetterChanges('a1b2c3')).toEqual([1, 1, 1]);
    });
});
// ... (rest of the code for context)
describe('countLetterChanges', () => {
    test('should count consecutive letters correctly', () => {
        const result: number[] = countLetterChanges("aaabbcdeee");
        expect(result).toEqual([3, 2, 1, 1, 3]);
    });

    test('should return an array with one count for a single character', () => {
        const result: number[] = countLetterChanges("a");
        expect(result).toEqual([1]);
    });

    test('should return counts for a string with no consecutive letters', () => {
        const result: number[] = countLetterChanges("abcdef");
        expect(result).toEqual([1, 1, 1, 1, 1, 1]);
    });

    test('should handle a string with only identical letters', () => {
        const result: number[] = countLetterChanges("rrrrrr");
        expect(result).toEqual([6]);
    });

    test('should handle a long string with random letters', () => {
        const result: number[] = countLetterChanges("xxxyyyzzzaaaab");
        expect(result).toEqual([3, 3, 3, 4, 1]);
    });

    test('should handle numeric characters in the string', () => {
        const result: number[] = countLetterChanges("1122334455");
        expect(result).toEqual([2, 2, 2, 2, 2]);
    });
});
