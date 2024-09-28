#include <unordered_map>
#include <string>

class TrieNode {
public:
    TrieNode() : is_end_of_word(false) {}

    bool hasChild(char ch) const {
        return children.find(ch) != children.end();
    }

    TrieNode* getChild(char ch) {
        auto it = children.find(ch);
        return it != children.end() ? it->second : nullptr;
    }

    void addChild(char ch) {
        if (children.find(ch) == children.end()) {
            children[ch] = new TrieNode();
        }
    }

    void setEndOfWord() {
        is_end_of_word = true;
    }

    bool isEnd() const {
        return is_end_of_word;
    }

private:
    std::unordered_map<char, TrieNode*> children;
    bool is_end_of_word;
};

class Trie {
public:
    Trie() : root(new TrieNode()) {}

    void insert(const std::string& word) {
        TrieNode* current = root;
        for (char ch : word) {
            current->addChild(ch);
            current = current->getChild(ch);
        }
        current->setEndOfWord();
    }

    bool search(const std::string& word) const {
        TrieNode* current = root;
        for (char ch : word) {
            if (!current->hasChild(ch)) {
                return false;
            }
            current = current->getChild(ch);
        }
        return current->isEnd();
    }

    bool startsWith(const std::string& prefix) const {
        TrieNode* current = root;
        for (char ch : prefix) {
            if (!current->hasChild(ch)) {
                return false;
            }
            current = current->getChild(ch);
        }
        return true;
    }

    ~Trie() {
        deleteTrie(root);
    }

private:
    TrieNode* root;

    void deleteTrie(TrieNode* node) {
        for (auto& [key, child] : node->children) {
            deleteTrie(child);
        }
        delete node;
    }
};