#include <iostream>
#include <unordered_map>
#include <string>

// TrieNode class
class TrieNode {
public:
    std::unordered_map<char, TrieNode*> children;
    bool is_end_of_word;

    TrieNode() : is_end_of_word(false) {}

    bool has_child(char ch) {
        return children.find(ch) != children.end();
    }

    TrieNode* get_child(char ch) {
        return children[ch];
    }

    void add_child(char ch) {
        if (!has_child(ch)) {
            children[ch] = new TrieNode();
        }
    }

    void set_end_of_word() {
        is_end_of_word = true;
    }

    bool is_end() const {
        return is_end_of_word;
    }

    ~TrieNode() {
        for (auto& child : children) {
            delete child.second;
        }
    }
};

// Trie class
class Trie {
public:
    TrieNode* root;

    Trie() : root(new TrieNode()) {}

    void insert(const std::string& word) {
        TrieNode* current = root;
        for (char ch : word) {
            current->add_child(ch);
            current = current->get_child(ch);
        }
        current->set_end_of_word();
    }

    bool search(const std::string& word) {
        TrieNode* current = root;
        for (char ch : word) {
            if (!current->has_child(ch)) {
                return false;
            }
            current = current->get_child(ch);
        }
        return current->is_end();
    }

    bool starts_with(const std::string& prefix) {
        TrieNode* current = root;
        for (char ch : prefix) {
            if (!current->has_child(ch)) {
                return false;
            }
            current = current->get_child(ch);
        }
        return true;
    }

    ~Trie() {
        delete root;
    }
};