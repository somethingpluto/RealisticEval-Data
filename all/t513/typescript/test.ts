describe('isPhraseInStringIgnoreCase', () => {
    it('should match exact phrases case-insensitively', () => {
        expect(isPhraseInStringIgnoreCase("hello world", "Hello World")).toBe(true);
    });

    it('should match partial words case-insensitively', () => {
        expect(isPhraseInStringIgnoreCase("Hello", "saying Hello there")).toBe(true);
    });

    it('should match different cases', () => {
        expect(isPhraseInStringIgnoreCase("HELLO", "hello there!")).toBe(true);
        expect(isPhraseInStringIgnoreCase("world", "WORLD is great")).toBe(true);
    });

    it('should not match non-existent phrases', () => {
        expect(isPhraseInStringIgnoreCase("goodbye", "Hello world")).toBe(false);
        expect(isPhraseInStringIgnoreCase("hello", "goodbye world")).toBe(false);
    });
});