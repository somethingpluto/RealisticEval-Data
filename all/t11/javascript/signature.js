/**
 * Implement a dictionary tree for fast string retrieval and storage
 */

class Trie {
    constructor() {
        /**
         * Initialize your data structure here.
         */
    }

    insert(word) {
        /**
         * Inserts a word into the trie.
         * @param {string} word - The word to be inserted.
         * @return {void}
         */
    }

    search(word) {
        /**
         * Returns if the word is in the trie.
         * @param {string} word - The word to search.
         * @return {boolean}
         */
    }

    startsWith(prefix) {
        /**
         * Returns if there is any word in the trie that starts with the given prefix.
         * @param {string} prefix - The prefix to check.
         * @return {boolean}
         */
    }
}

class TrieNode {
    constructor() {
        this.children = {};
    }
}