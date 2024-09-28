#include <iostream>
#include <vector>
#include <stack>

struct TreeNode {
    int value;
    TreeNode* left;
    TreeNode* right;
    
    // Constructor for TreeNode
    TreeNode(int val = 0, TreeNode* l = nullptr, TreeNode* r = nullptr) 
        : value(val), left(l), right(r) {}
};

class BinaryTree {
public:
    TreeNode* root;

    // Constructor for BinaryTree
    BinaryTree(TreeNode* r = nullptr) : root(r) {}

    // Recursive Preorder Traversal
    std::vector<int> preorderTraversal(TreeNode* node) {
        std::vector<int> result;
        preorderHelper(node, result);
        return result;
    }

    // Recursive Inorder Traversal
    std::vector<int> inorderTraversal(TreeNode* node) {
        std::vector<int> result;
        inorderHelper(node, result);
        return result;
    }

    // Recursive Postorder Traversal
    std::vector<int> postorderTraversal(TreeNode* node) {
        std::vector<int> result;
        postorderHelper(node, result);
        return result;
    }

    // Iterative Preorder Traversal
    std::vector<int> iterativePreorder() {
        std::vector<int> result;
        if (!root) return result;
        std::stack<TreeNode*> stack;
        stack.push(root);
        while (!stack.empty()) {
            TreeNode* node = stack.top();
            stack.pop();
            if (node) {
                result.push_back(node->value);
                stack.push(node->right);
                stack.push(node->left);
            }
        }
        return result;
    }

    // Iterative Inorder Traversal
    std::vector<int> iterativeInorder() {
        std::vector<int> result;
        std::stack<TreeNode*> stack;
        TreeNode* current = root;
        while (current || !stack.empty()) {
            while (current) {
                stack.push(current);
                current = current->left;
            }
            current = stack.top();
            stack.pop();
            result.push_back(current->value);
            current = current->right;
        }
        return result;
    }

    // Iterative Postorder Traversal
    std::vector<int> iterativePostorder() {
        std::vector<int> result;
        if (!root) return result;
        std::stack<TreeNode*> stack;
        stack.push(root);
        while (!stack.empty()) {
            TreeNode* node = stack.top();
            stack.pop();
            result.insert(result.begin(), node->value);
            if (node->left) {
                stack.push(node->left);
            }
            if (node->right) {
                stack.push(node->right);
            }
        }
        return result;
    }

private:
    void preorderHelper(TreeNode* node, std::vector<int>& result) {
        if (node) {
            result.push_back(node->value);
            preorderHelper(node->left, result);
            preorderHelper(node->right, result);
        }
    }

    void inorderHelper(TreeNode* node, std::vector<int>& result) {
        if (node) {
            inorderHelper(node->left, result);
            result.push_back(node->value);
            inorderHelper(node->right, result);
        }
    }

    void postorderHelper(TreeNode* node, std::vector<int>& result) {
        if (node) {
            postorderHelper(node->left, result);
            postorderHelper(node->right, result);
            result.push_back(node->value);
        }
    }
};

int main() {
    // Example usage:
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    BinaryTree tree(root);

    std::vector<int> preorder = tree.preorderTraversal(root);
    std::cout << "Recursive Preorder: ";
    for (int val : preorder) std::cout << val << " ";
    std::cout << std::endl;

    std::vector<int> inorder = tree.inorderTraversal(root);
    std::cout << "Recursive Inorder: ";
    for (int val : inorder) std::cout << val << " ";
    std::cout << std::endl;

    std::vector<int> postorder = tree.postorderTraversal(root);
    std::cout << "Recursive Postorder: ";
    for (int val : postorder) std::cout << val << " ";
    std::cout << std::endl;

    std::vector<int> itPreorder = tree.iterativePreorder();
    std::cout << "Iterative Preorder: ";
    for (int val : itPreorder) std::cout << val << " ";
    std::cout << std::endl;

    std::vector<int> itInorder = tree.iterativeInorder();
    std::cout << "Iterative Inorder: ";
    for (int val : itInorder) std::cout << val << " ";
    std::cout << std::endl;

    std::vector<int> itPostorder = tree.iterativePostorder();
    std::cout << "Iterative Postorder: ";
    for (int val : itPostorder) std::cout << val << " ";
    std::cout << std::endl;
    
    // Clean up manually allocated memory
    delete root->left->left;
    delete root->left->right;
    delete root->left;
    delete root->right;
    delete root;

    return 0;
}