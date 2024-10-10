#include <iostream>
#include <vector>

// Define the TreeNode structure
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int key) : val(key), left(nullptr), right(nullptr) {}
};

// Define the BinaryTree class
class BinaryTree {
private:
    TreeNode* root;

    // Helper function for insertion
    void _insert(TreeNode*& node, int key);

    // Helper function for inorder traversal
    void _inorderTraversal(TreeNode* node, std::vector<int>& result);

    // Helper function for preorder traversal
    void _preorderTraversal(TreeNode* node, std::vector<int>& result);

    // Helper function for postorder traversal
    void _postorderTraversal(TreeNode* node, std::vector<int>& result);

public:
    BinaryTree() : root(nullptr) {}

    // Function to insert a new key into the binary tree
    void insert(int key);

    // Function to perform inorder traversal
    std::vector<int> inorderTraversal();

    // Function to perform preorder traversal
    std::vector<int> preorderTraversal();

    // Function to perform postorder traversal
    std::vector<int> postorderTraversal();
};

// Implementation of helper functions
void BinaryTree::_insert(TreeNode*& node, int key) {
    if (node == nullptr) {
        node = new TreeNode(key);
    } else if (key < node->val) {
        _insert(node->left, key);
    } else {
        _insert(node->right, key);
    }
}

void BinaryTree::_inorderTraversal(TreeNode* node, std::vector<int>& result) {
    if (node != nullptr) {
        _inorderTraversal(node->left, result);
        result.push_back(node->val);
        _inorderTraversal(node->right, result);
    }
}

void BinaryTree::_preorderTraversal(TreeNode* node, std::vector<int>& result) {
    if (node != nullptr) {
        result.push_back(node->val);
        _preorderTraversal(node->left, result);
        _preorderTraversal(node->right, result);
    }
}

void BinaryTree::_postorderTraversal(TreeNode* node, std::vector<int>& result) {
    if (node != nullptr) {
        _postorderTraversal(node->left, result);
        _postorderTraversal(node->right, result);
        result.push_back(node->val);
    }
}

// Public member functions
void BinaryTree::insert(int key) {
    _insert(root, key);
}

std::vector<int> BinaryTree::inorderTraversal() {
    std::vector<int> result;
    _inorderTraversal(root, result);
    return result;
}

std::vector<int> BinaryTree::preorderTraversal() {
    std::vector<int> result;
    _preorderTraversal(root, result);
    return result;
}

std::vector<int> BinaryTree::postorderTraversal() {
    std::vector<int> result;
    _postorderTraversal(root, result);
    return result;
}
