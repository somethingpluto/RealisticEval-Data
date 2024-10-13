describe('Trie', () => {
    let trie;

    beforeEach(() => {
        trie = new Trie();
        trie.insert("apple");
        trie.insert("app");
        trie.insert("apricot");
        trie.insert("banana");
        trie.insert("carrot");
        trie.insert("car");
        trie.insert("care");
        trie.insert("");
        trie.insert("Hello");
        trie.insert("hello");
    });

    describe('basic search', () => {
        it('should find words that exist in the trie', () => {
            expect(trie.search("apple")).toBe(true);
            expect(trie.search("app")).toBe(true);
            expect(trie.search("apricot")).toBe(true);
        });
    });

    describe('unsuccessful search', () => {
        it('should not find words that do not exist in the trie', () => {
            expect(trie.search("bandana")).toBe(false);
        });
    });

    describe('prefix search', () => {
        it('should find prefixes that exist in the trie', () => {
            expect(trie.startsWith("car")).toBe(true);
            expect(trie.startsWith("care")).toBe(true);
            expect(trie.startsWith("cat")).toBe(false);
        });
    });

    describe('empty string', () => {
        it('should handle empty strings correctly', () => {
            expect(trie.search("")).toBe(true);
            expect(trie.startsWith("")).toBe(true);
        });
    });

    describe('case sensitivity', () => {
        it('should handle case sensitivity correctly', () => {
            expect(trie.search("Hello")).toBe(true);
            expect(trie.search("hello")).toBe(true);
            expect(trie.search("HELLO")).toBe(false);
        });
    });
});