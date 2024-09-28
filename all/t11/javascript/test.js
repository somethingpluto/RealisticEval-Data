const Trie = require('./Trie'); // Adjust the path as necessary

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

    test('basic search', () => {
        expect(trie.search("apple")).toBe(true);
        expect(trie.search("app")).toBe(true);
        expect(trie.search("apricot")).toBe(true);
    });

    test('unsuccessful search', () => {
        expect(trie.search("bandana")).toBe(false);
    });

    test('prefix search', () => {
        expect(trie.startsWith("car")).toBe(true);
        expect(trie.startsWith("care")).toBe(true);
        expect(trie.startsWith("cat")).toBe(false);
    });

    test('empty string', () => {
        expect(trie.search("")).toBe(true);
        expect(trie.startsWith("")).toBe(true);
    });

    test('case sensitivity', () => {
        expect(trie.search("Hello")).toBe(true);
        expect(trie.search("hello")).toBe(true);
        expect(trie.search("HELLO")).toBe(false);
    });
});