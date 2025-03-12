/**
 * Check if the given phrase exists in the target string, ignoring case and allowing for variations in whitespace.
 *
 * @param {string} phrase - The phrase to search for in the string.
 * @param {string} string - The target string in which to search for the phrase.
 * @returns {boolean} - True if the phrase is found as a whole word in the string, False otherwise.
 */
function isPhraseInStringIgnoreCase(phrase, string) {
    // Normalize both the phrase and the string by removing extra whitespaces and converting to lowercase
    const normalizedPhrase = phrase.trim().replace(/\s+/g, ' ').toLowerCase();
    const normalizedString = string.trim().replace(/\s+/g, ' ').toLowerCase();

    // Create a regex pattern that matches the phrase as a whole word
    const regexPattern = new RegExp(`\\b${normalizedPhrase}\\b`);

    // Test the regex pattern against the normalized string
    return regexPattern.test(normalizedString);
}
describe('TestIsPhraseInStringIgnoreCase', () => {
    describe('test_exact_match_case_insensitive', () => {
        it('should find an exact match case-insensitively', () => {
            expect(isPhraseInStringIgnoreCase("hello world", "Hello World")).toBe(true);
        });
    });

    describe('test_partial_word_match_case_insensitive', () => {
        it('should find a partial word match case-insensitively', () => {
            expect(isPhraseInStringIgnoreCase("Hello", "saying Hello there")).toBe(true);
        });
    });

    describe('test_different_cases', () => {
        it('should find phrases with different cases', () => {
            expect(isPhraseInStringIgnoreCase("HELLO", "hello there!")).toBe(true);
            expect(isPhraseInStringIgnoreCase("world", "WORLD is great")).toBe(true);
        });
    });

    describe('test_non_existent_phrase', () => {
        it('should not find non-existent phrases', () => {
            expect(isPhraseInStringIgnoreCase("goodbye", "Hello world")).toBe(false);
            expect(isPhraseInStringIgnoreCase("hello", "goodbye world")).toBe(false);
        });
    });
});

