package org.real.temp;

public class Answer {
    public static class Trie {
        /**
         * Implement a dictionary tree for fast string retrieval and storage
         */

        private TrieNode root;

        public Trie() {
            root = new TrieNode();
        }

        public void insert(String word) {
            TrieNode node = root;
            for (char c : word.toCharArray()) {
                if (!node.children.containsKey(c)) {
                    node.children.put(c, new TrieNode());
                }
                node = node.children.get(c);
            }
            node.isEndOfWord = true;
        }

        public boolean search(String word) {
            TrieNode node = searchPrefix(word);
            return node != null && node.isEndOfWord;
        }

        public boolean startsWith(String prefix) {
            return searchPrefix(prefix) != null;
        }

        private TrieNode searchPrefix(String prefix) {
            TrieNode node = root;
            for (char c : prefix.toCharArray()) {
                if (!node.children.containsKey(c)) {
                    return null;
                }
                node = node.children.get(c);
            }
            return node;
        }
    }

    public static class TrieNode {
        private boolean isEndOfWord;
        private final Map<Character, TrieNode> children;

        public TrieNode() {
            isEndOfWord = false;
            children = new HashMap<>();
        }
    }
}