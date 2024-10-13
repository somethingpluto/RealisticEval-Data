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