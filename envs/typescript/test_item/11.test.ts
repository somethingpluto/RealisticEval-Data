import { EventEmitter } from 'events';

/**
 * Implements a dictionary tree (Trie) for fast string retrieval and storage.
 * @extends EventEmitter
 */
class Trie extends EventEmitter {
  private root: TrieNode;

  constructor() {
    super();
    this.root = new TrieNode();
  }

  /**
   * Inserts a word into the trie.
   * @param word The word to insert.
   */
  insert(word: string): void {
    let node = this.root;
    for (const char of word) {
      if (!node.children[char]) {
        node.children[char] = new TrieNode();
      }
      node = node.children[char];
    }
    node.isEndOfWord = true;
    this.emit('insert', word);
  }

  /**
   * Searches for a word in the trie.
   * @param word The word to search for.
   * @returns true if the word is found, false otherwise.
   */
  search(word: string): boolean {
    let node = this.root;
    for (const char of word) {
      if (!node.children[char]) {
        return false;
      }
      node = node.children[char];
    }
    return node.isEndOfWord;
  }

  /**
   * Checks if there is any word in the trie that starts with the given prefix.
   * @param prefix The prefix to check.
   * @returns true if there is any word starting with the prefix, false otherwise.
   */
  startsWith(prefix: string): boolean {
    let node = this.root;
    for (const char of prefix) {
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
  children: { [key: string]: TrieNode };
  isEndOfWord: boolean;

  constructor() {
    this.children = {};
    this.isEndOfWord = false;
  }
}
describe('Trie', () => {
    let trie: Trie;
  
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
  
    it('should search for basic words', () => {
      expect(trie.search("apple")).toBe(true);
      expect(trie.search("app")).toBe(true);
      expect(trie.search("apricot")).toBe(true);
    });
  
    it('should handle unsuccessful searches', () => {
      expect(trie.search("bandana")).toBe(false);
    });
  
    it('should handle prefix searches', () => {
      expect(trie.startsWith("car")).toBe(true);
      expect(trie.startsWith("care")).toBe(true);
      expect(trie.startsWith("cat")).toBe(false);
    });
  
    it('should handle empty strings', () => {
      expect(trie.search("")).toBe(true);
      expect(trie.startsWith("")).toBe(true);
    });
  
    it('should handle case sensitivity', () => {
      expect(trie.search("Hello")).toBe(true);
      expect(trie.search("hello")).toBe(true);
      expect(trie.search("HELLO")).toBe(false);
    });
  });
