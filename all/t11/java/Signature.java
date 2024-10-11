/**
 * Implement a dictionary tree for fast string retrieval and storage
 */
public class Trie {
    
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    /**
     * Inserts a word into the trie.
     *
     * @param word the word to be inserted
     */
    public void insert(String word) {}

    /**
     * Returns if the word is in the trie.
     *
     * @param word the word to search
     * @return true if the word exists in the trie, false otherwise
     */
    public boolean search(String word) {}

    /**
     * Returns if there is any word in the trie that starts with the given prefix.
     *
     * @param prefix the prefix to search
     * @return true if there is any word starting with the prefix, false otherwise
     */
    public boolean startsWith(String prefix) {}
}

/**
 * Represents a node in the trie.
 */
class TrieNode {
    private Map<Character, TrieNode> children;

    public TrieNode() {
        children = new HashMap<>();
    }

    /**
     * Gets the child node associated with the given character.
     *
     * @param ch the character to look up
     * @return the child node or null if it does not exist
     */
    public TrieNode getChild(char ch) {}

    /**
     * Adds a child node associated with the given character.
     *
     * @param ch the character to add
     * @param node the child node to add
     */
    public void addChild(char ch, TrieNode node) {}

    /**
     * Checks if this node has any children.
     *
     * @return true if this node has no children, false otherwise
     */
    public boolean hasChildren() {}
}