// TrieNode class
class TrieNode {
public:
    std::unordered_map<char, TrieNode*> children;

    TrieNode() {}
};

// Trie class
class Trie {
public:
    /**
     * Implement a dictionary tree for fast string retrieval and storage
     */
    TrieNode* root;

    Trie() : root(new TrieNode()) {}

    ~Trie() {
        delete root;
    }

    // Insert a word into the trie
    void insert(const std::string& word);

    // Search for a word in the trie
    bool search(const std::string& word);

    // Check if there is any word in the trie that starts with the given prefix
    bool starts_with(const std::string& prefix);
};

// Implementation of the insert method
void Trie::insert(const std::string& word) {
    // Implementation goes here
    // ...
}

// Implementation of the search method
bool Trie::search(const std::string& word) {
    // Implementation goes here
    // ...
}

// Implementation of the starts_with method
bool Trie::starts_with(const std::string& prefix) {
    // Implementation goes here
    // ...
}