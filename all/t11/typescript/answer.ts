class TrieNode {
    children: { [key: string]: TrieNode };
    isEndOfWord: boolean;
  
    constructor() {
      this.children = {};
      this.isEndOfWord = false;
    }
  
    hasChild(ch: string): boolean {
      return ch in this.children;
    }
  
    getChild(ch: string): TrieNode | undefined {
      return this.children[ch];
    }
  
    addChild(ch: string): void {
      if (!this.hasChild(ch)) {
        this.children[ch] = new TrieNode();
      }
    }
  
    setEndOfWord(): void {
      this.isEndOfWord = true;
    }
  
    isEnd(): boolean {
      return this.isEndOfWord;
    }
  }
  
  class Trie {
    root: TrieNode;
  
    constructor() {
      this.root = new TrieNode();
    }
  
    insert(word: string): void {
      let current = this.root;
      for (const ch of word) {
        current.addChild(ch);
        current = current.getChild(ch)!;
      }
      current.setEndOfWord();
    }
  
    search(word: string): boolean {
      let current = this.root;
      for (const ch of word) {
        if (!current.hasChild(ch)) {
          return false;
        }
        current = current.getChild(ch)!;
      }
      return current.isEnd();
    }
  
    startsWith(prefix: string): boolean {
      let current = this.root;
      for (const ch of prefix) {
        if (!current.hasChild(ch)) {
          return false;
        }
        current = current.getChild(ch)!;
      }
      return true;
    }
  }