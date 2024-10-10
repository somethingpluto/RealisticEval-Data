#include <iostream>
#include <vector>

// Define the TreeNode structure
struct TreeNode {
    int value;
    TreeNode* left;
    TreeNode* right;

    // Constructor
    TreeNode(int val = 0) : value(val), left(nullptr), right(nullptr) {}
};

// Define the BinaryTree class
class BinaryTree {
private:
    TreeNode* root;

public:
    // Constructor
    BinaryTree(TreeNode* root = nullptr) : root(root) {}

    // Preorder traversal
    void preorderTraversal(TreeNode* node, std::vector<int>& result) const {
        if (node != nullptr) {
            result.push_back(node->value);
            preorderTraversal(node->left, result);
            preorderTraversal(node->right, result);
        }
    }

    // Inorder traversal
    void inorderTraversal(TreeNode* node, std::vector<int>& result) const {
        if (node != nullptr) {
            inorderTraversal(node->left, result);
            result.push_back(node->value);
            inorderTraversal(node->right, result);
        }
    }

    // Postorder traversal
    void postorderTraversal(TreeNode* node, std::vector<int>& result) const {
        if (node != nullptr) {
            postorderTraversal(node->left, result);
            postorderTraversal(node->right, result);
            result.push_back(node->value);
        }
    }

    // Helper functions to start traversals from the root
    std::vector<int> getPreorderTraversal() const {
        std::vector<int> result;
        preorderTraversal(root, result);
        return result;
    }

    std::vector<int> getInorderTraversal() const {
        std::vector<int> result;
        inorderTraversal(root, result);
        return result;
    }

    std::vector<int> getPostorderTraversal() const {
        std::vector<int> result;
        postorderTraversal(root, result);
        return result;
    }
};