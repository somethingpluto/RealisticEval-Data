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
