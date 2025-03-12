/**
 * Implements a dictionary tree (Trie) for fast string retrieval and storage.
 */
class Trie {
    /**
     * Constructs a new Trie.
     */
    constructor() {
        this.root = new TrieNode();
    }

    /**
     * Inserts a word into the trie.
     * @param {string} word - The word to insert.
     */
    insert(word) {
        let node = this.root;
        for (let char of word) {
            if (!node.children[char]) {
                node.children[char] = new TrieNode();
            }
            node = node.children[char];
        }
        node.isEndOfWord = true;
    }

    /**
     * Searches for a word in the trie.
     * @param {string} word - The word to search for.
     * @returns {boolean} - Returns true if the word is found, false otherwise.
     */
    search(word) {
        let node = this.root;
        for (let char of word) {
            if (!node.children[char]) {
                return false;
            }
            node = node.children[char];
        }
        return node.isEndOfWord === true;
    }

    /**
     * Checks if there is any word in the trie that starts with the given prefix.
     * @param {string} prefix - The prefix to check.
     * @returns {boolean} - Returns true if there is any word with the prefix, false otherwise.
     */
    startsWith(prefix) {
        let node = this.root;
        for (let char of prefix) {
            if (!node.children[char]) {
                return false;
            }
            node = node.children[char];
        }
        return true;
    }
}

/**
 * Represents a node in the Trie.
 */
class TrieNode {
    /**
     * Constructs a new TrieNode.
     */
    constructor() {
        this.children = {};
        this.isEndOfWord = false;
    }
}
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
