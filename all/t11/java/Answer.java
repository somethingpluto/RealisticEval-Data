package org.real.temp;

public class Answer {

    static class TrieNode {
        private final java.util.Map<Character, TrieNode> children = new java.util.HashMap<>();
        private boolean isEndOfWord;

        public boolean hasChild(char ch) {
            return children.containsKey(ch);
        }

        public TrieNode getChild(char ch) {
            return children.get(ch);
        }

        public void addChild(char ch) {
            if (!children.containsKey(ch)) {
                children.put(ch, new TrieNode());
            }
        }

        public void setEndOfWord() {
            this.isEndOfWord = true;
        }

        public boolean isEnd() {
            return this.isEndOfWord;
        }
    }

    static class Trie {
        private final TrieNode root;

        public Trie() {
            this.root = new TrieNode();
        }

        public void insert(String word) {
            TrieNode current = this.root;
            for (char ch : word.toCharArray()) {
                current.addChild(ch);
                current = current.getChild(ch);
            }
            current.setEndOfWord();
        }

        public boolean search(String word) {
            TrieNode current = this.root;
            for (char ch : word.toCharArray()) {
                if (!current.hasChild(ch)) {
                    return false;
                }
                current = current.getChild(ch);
            }
            return current.isEnd();
        }

        public boolean startsWith(String prefix) {
            TrieNode current = this.root;
            for (char ch : prefix.toCharArray()) {
                if (!current.hasChild(ch)) {
                    return false;
                }
                current = current.getChild(ch);
            }
            return true;
        }
    }

    public static void main(String[] args) {
        // Example usage
        Trie trie = new Trie();
        trie.insert("hello");
        trie.insert("world");

        System.out.println(trie.search("hello")); // Should print true
        System.out.println(trie.startsWith("he")); // Should print true
        System.out.println(trie.search("worlds")); // Should print false
    }
}