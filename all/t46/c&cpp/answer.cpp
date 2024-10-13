#include <iostream>
#include <vector>
using namespace std;

// TreeNode class definition
class TreeNode {
public:
    int value;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int val = 0, TreeNode* l = nullptr, TreeNode* r = nullptr) : value(val), left(l), right(r) {}
};

// BinaryTree class definition
class BinaryTree {
public:
    TreeNode* root;

    BinaryTree(TreeNode* r = nullptr) : root(r) {}

    // Recursive Preorder Traversal
    vector<int> preorder_traversal(TreeNode* node, vector<int>* result = nullptr) {
        if (result == nullptr) {
            result = new vector<int>();
        }
        if (node != nullptr) {
            result->push_back(node->value);
            preorder_traversal(node->left, result);
            preorder_traversal(node->right, result);
        }
        return *result;
    }

    // Recursive Inorder Traversal
    vector<int> inorder_traversal(TreeNode* node, vector<int>* result = nullptr) {
        if (result == nullptr) {
            result = new vector<int>();
        }
        if (node != nullptr) {
            inorder_traversal(node->left, result);
            result->push_back(node->value);
            inorder_traversal(node->right, result);
        }
        return *result;
    }

    // Recursive Postorder Traversal
    vector<int> postorder_traversal(TreeNode* node, vector<int>* result = nullptr) {
        if (result == nullptr) {
            result = new vector<int>();
        }
        if (node != nullptr) {
            postorder_traversal(node->left, result);
            postorder_traversal(node->right, result);
            result->push_back(node->value);
        }
        return *result;
    }

    // Iterative Preorder Traversal
    vector<int> iterative_preorder() {
        if (root == nullptr) {
            return {};
        }
        vector<int> result;
        vector<TreeNode*> stack = {root};
        while (!stack.empty()) {
            TreeNode* node = stack.back();
            stack.pop_back();
            if (node != nullptr) {
                result.push_back(node->value);
                stack.push_back(node->right);
                stack.push_back(node->left);
            }
        }
        return result;
    }

    // Iterative Inorder Traversal
    vector<int> iterative_inorder() {
        vector<int> result;
        vector<TreeNode*> stack;
        TreeNode* current = root;
        while (!stack.empty() || current != nullptr) {
            while (current != nullptr) {
                stack.push_back(current);
                current = current->left;
            }
            current = stack.back();
            stack.pop_back();
            result.push_back(current->value);
            current = current->right;
        }
        return result;
    }

    // Iterative Postorder Traversal
    vector<int> iterative_postorder() {
        if (root == nullptr) {
            return {};
        }
        vector<int> result;
        vector<TreeNode*> stack = {root};
        while (!stack.empty()) {
            TreeNode* node = stack.back();
            stack.pop_back();
            result.insert(result.begin(), node->value);
            if (node->left != nullptr) {
                stack.push_back(node->left);
            }
            if (node->right != nullptr) {
                stack.push_back(node->right);
            }
        }
        return result;
    }
};